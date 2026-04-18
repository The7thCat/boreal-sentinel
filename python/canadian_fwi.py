

def canadian_fwi(ds_daily):
    T = ds_daily["t2m"] - 273.15
    RH = compute_rh(ds_daily)
    wind = compute_wind(ds_daily)
    rain = ds_daily["tp"] * 1000 # m to mm

    ffmc = ffmx_step(T, RH, wind, rain)
    dmc = dmc_step(T, RH, rain)
    dc = dc_step(T, rain)
    isi = isi_step(ffmc, wind)
    bui = bui_step(dmc, dc)
    fwi = fwi_step(isi, bui)

    return xr.Dataset({
        "FFMC": ffmc,
        "DMC": dmc,
        "DC": dc,
        "ISI": isi,
        "BUI": bui,
        "FWI": fwi,
    })