from scipy.spatial import Delaunay
import numpy as np

def triangulate_era5(ds):
    lats = ds["latitude"].values
    lons = ds["longitude"].values

    grid = np.array([(lat, lon) for lat in lats for lon in lons])
    tri = Delaunay(grid)

    return tri
