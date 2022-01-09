

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem import geo
import numpy as np




def run():
    """Prints the closest 10 and the furthest 10 stations from Cambridge, along with their distances."""

    # Build list of stations
    stations = build_station_list()

    # Coordinates of Cambridge city centre
    cam = (52.2053, 0.1218)

    # Radius value in km
    r = 10

    # Create the list of stations within given radius
    stations_within = geo.stations_within_radius(stations, cam, r)

    # Extract just the names of the stations and sort them
    stations_new = []
    for s in stations_within:
        stations_new.append(s.name)
    stations_new.sort()

    # Print the results
    print(stations_new)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

