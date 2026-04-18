# pipelines/synop_pipeline.py

from ingestion.synop import fetch_and_decode
from processing.time import normalize_timestamp
from processing.features import simple_fire_index
from utils.io import save_dataframe

def run_synop_pipeline(stations):
    df = fetch_and_decode(stations)
    df = normalize_timestamp(df)
    df = simple_fire_index(df)

    save_dataframe(df, "data/processed/synop.parquet")

    return df