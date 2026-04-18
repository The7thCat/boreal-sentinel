def simple_fire_index(df):

    df["simple_index"] = (
        df["temperature_C"] *
        (1 - df["dewpoint_C"] / df["temperature_C"]) *
        df["wind_speed_ms"]
    )
    return df