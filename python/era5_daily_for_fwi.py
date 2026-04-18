
def era5daily_for_fwi(ds_3h):

    ds_daily = ds_3h.sel(time=ds_3h.time.dt.hour == 12)

    ds_daily.to_netcdf("data/processed/era5_daily.nc")
    return ds_daily

