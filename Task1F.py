from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1F"""
    stations = build_station_list()
    # Builds a list of inconsistent stations
    inconsistent_station_list = inconsistent_typical_range_stations(stations)
    # Initialise array to contain station names
    inconsistent_station_names = []
    #Add the station names to the list of names
    for station in inconsistent_station_list:
        inconsistent_station_names.append(station.name)
    print(sorted(inconsistent_station_names))



if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
 