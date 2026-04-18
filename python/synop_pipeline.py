import pandas as pd
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor

from config.synop_parser import decode_synop


def fetch_and_decode(station_id):
    raw = fetch_synop(station_id)
    if not raw:
        return None

    decoded = decode_synop(raw)

    # Zeit aus SYNOP-Header extrahieren
    # AAXX DDHHMM
    parts = raw.split()
    header = parts[1] # DDHHMM
    day = int(header[:2])
    hour = int(header[2:4])

    now = datetime.now(timezone.utc)
    timestamp = datetime(now.year, now.month, day, hour)

    return decoded

def synop_dataframe(stations):
    rows = []

    with ThreadPoolExecutor(max_workers=6) as ex:
        for result in ex.map(fetch_and_decode, stations):
            if result:
                rows.append(result)

    return pd.DataFrame(rows)