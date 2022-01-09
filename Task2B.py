from floodsystem import station
from floodsystem import flood
from floodsystem.stationdata import build_station_list
from floodsystem import stationdata

def run():
    """Requirements for Task 2B"""
    stations = build_station_list()
    stationdata.update_water_levels(stations)
    stations_over_threshold = flood.stations_level_over_threshold(stations, 0.8)
    for station in stations_over_threshold:
        print(station[0].name, station[1])



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()