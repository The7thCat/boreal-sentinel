from config.synop_parser import fetch_synop, decode_synop
from weatherstations import stations

# fetch synop from weatherstations
for sid in stations:
    synop = fetch_synop(sid)
    if synop:
        print(sid, decode_synop(synop))
    else:
        print(sid, "no data")