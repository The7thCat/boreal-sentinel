import os
from logging import Filter
from region import BBOX
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()
MAP_KEY = os.getenv("NASA_FIRMS_KEY")

url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{MAP_KEY}/VIIRS_SNPP_NRT/Europe"

df = pd.read_csv(url)

# ding Box Filter
# = A fast, noise‑robust edge detector based on the difference of two box filters.
# Highlights weak edges by subtracting a large smoothing window from a smaller one.
# Useful for satellite imagery, segmentation, and general edge enhancement.

df = df[
    (df.latitude >= BBOX["south"]) &
    (df.latitude <= BBOX["north"]) &
    (df.latitude >= BBOX["west"]) &
    (df.latitude <= BBOX["east"])
]

df.to_csv("data/raw/hotspots.csv", index=False)

