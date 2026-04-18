import requests
import re

"""WMO GTS
GTS = Global Telecommunication System
worldwide free available weather data.
Downside: ASCII-telegrams , no json, no rest. Only 3 hourly updates.
lol? - WMO is based on telegram specifications from the 1960s.
"""


# SYNOP = SYNchronized Observation, telegram that contains weatherdata
# in one line
# synop block is inside a html pre-block


#  SYNOP fetcher
def fetch_synop(station_id):
    url = f"https://ogimet.com/cgi-bin/gsynres?ind={station_id}&lang=en&decoded=no"
    html = requests.get(url).text

    match = re.search(r"<pre>(.*?)</pre>", html, re.DOTALL)
    if not match:
        return None

    text = match.group(1)

# AAXX = header start marker for synop telegram

    for line in text.splitlines():
        if line.startswith("AAXX"):
            return line.strip()
        return None

# synops decoder

def decode_synop(synop_text):
    parts = synop_text.split()
    result = {}

    # temperature (1SnTTT)
    temp = next((p for p in parts if re.match(r"1\d{4}", p)), None)
    if temp:
        sign = -1 if temp[1] == "1" else 1
        result["temperature_C"] = sign * (int(temp[2:]) / 10)

    # dew point (2SnTTT)
    dew = next((p for p in parts if re.match(r"2\d{4}", p)), None)
    if dew:
        sign = -1 if dew[1] == "1" else 1
        result["dewpoint_C"] = sign * (int(dew[2:]) / 10)

    #air pressure (3PPPP)
    pres = next((p for p in parts if re.match(r"3\d{4}", p)), None)
    if pres:
        result["pressure_hPa"] = int(pres[1:]) / 10

    #windspeed (00fff)
    wind = next((p for p in parts if re.match(r"00\d{3}", p)), None)
    if wind:
        result["wind_speed_ms"] = int(wind[2:])

    #wind direction
    winddir = next((p for p in parts if re.match(r"\d{5}", p)), None)
    if winddir:
        result["wind_direction_deg"] = int(winddir[:2]) * 10  # 36 = 360°

    # line of sight
    vis = next((p for p in parts if re.match(r"\d{2}", p)), None)
    if vis and len(vis) == 2:
        try:
            vv = int(vis)
            if vv <= 50:
                result["visibility_m"] = vv * 100
            elif vv <= 80:
                result["visibility_m"] = 5000 + (vv - 50) * 1000
            else:
                result["visibility_m"] = 30000  # "unlimited"
        except:
            pass

    # precipitation (6RRRt)
    rain = next((p for p in parts if re.match(r"6\d{3}\d", p)), None)
    if rain:
        RRR = int(rain[1:4])
        if RRR == 990:
            result["precip_mm"] = 0
        elif 0 <= RRR <= 989:
            result["precip_mm"] = RRR / 10

    # printing trend (5appp)
    trend = next((p for p in parts if re.match(r"5\d{4}", p)), None)
    if trend:
        a = int(trend[1])  # Tendenzcode
        ppp = int(trend[2:])  # Änderung in 0.1 hPa
        result["pressure_tendency_code"] = a
        result["pressure_change_hPa"] = ppp / 10

    return result
