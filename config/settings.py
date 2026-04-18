from dataclasses import dataclass

# file contains all constants, stations and boundary box data

SYNOP_STATIONS = [
    "26242",  # Tartu-Tõravere (EE)
    "26231",  # Jõgeva (EE)
    "26422",  # Rēzekne (LV)
    "26406",  # Daugavpils (LV)
    "26413",  # Gulbene (LV)
    "26411",  # Alūksne (LV)
]


@dataclass
class BoundingBox:
    north: float
    south: float
    west: float
    east: float

BBOX = BoundingBox(
    north=57.95,
    south=57.45,
    west=26.00,
    east=27.00,
)

REGION_NAME = "Voru-Valga-Aluksne"
