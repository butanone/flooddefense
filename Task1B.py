

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem import geo
import numpy as np




def run():
    """Prints the closest 10 and the furthest 10 stations from Cambridge, along with their distances."""

    # Build list of stations
    stations = build_station_list()

    # Build the sorted list of tuples (Station, distance)
    new_stations = geo.stations_by_distance(stations, (52.2053, 0.1218))

    # Build another list by extracting just the name and town from the station element
    sorted_stations=[]
    for s in new_stations:
        sorted_stations.append((s[0].name, s[0].town, s[1]))

    # Print the first and last 10 results
    print(sorted_stations[:10])
    print('\n')
    print(sorted_stations[-10:])
   


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

