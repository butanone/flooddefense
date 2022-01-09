from floodsystem import flood
from floodsystem.stationdata import build_station_list
from floodsystem import stationdata

def run():
    """Requirements for Task 2C"""
    stations = build_station_list()
    stationdata.update_water_levels(stations)
    high_risk_stations = flood.stations_highest_rel_level(stations,10)
    for station in high_risk_stations:
        print(station[0].name, station[1])

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()