from config.synop_parser import fetch_synop, decode_synop
from config.settings import SYNOP_STATIONS

# fetch synop from weatherstations
for sid in SYNOP_STATIONS:
    synop = fetch_synop(sid)
    if synop:
        print(sid, decode_synop(synop))
    else:
        print(sid, "no data")