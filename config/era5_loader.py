import cdsapi
from config.settings import BBOX

c = cdsapi.Client()

area = [
    BBOX["north"],
    BBOX["west"],
    BBOX["south"],
    BBOX["east"]
]

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': [
            '2m_temperature', 'total_precipitation', 'surface_pressure',
            '10m_u_component_of_wind', '10m_v_component_of_wind',
        ],
        'year': '2024',
        'month': '07',
        'day': ['01', '02', '03'],
        'time': [f'{h:02d}:00' for h in range(24)],
        'area': area,
        'format': "netcdf"
    },
    "data/raw/era5.nc"
)