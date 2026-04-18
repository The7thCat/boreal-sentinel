import xarray as xr

def era5_to_3h(path="data/raw/era5.nc"):
    ds = xr.open_dataset(path)

    ds_3h = ds.resample(time='3H').mean()

    ds_3h.to_netcdf("data/processed/era5_3h.nc")
    return ds_3h