import rasterio
import numpy as np

with rasterio.open("B04.jp2") as red, rasterio.open("B08.jp2") as nir:
    red_data = red.read(1).astype(float)
    nir_data = nir.read(1).astype(float)

    ndvi = (nir_data - red_data) / (nir_data + red_data)