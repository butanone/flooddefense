from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem import flood, plot, stationdata, geo, analysis
import datetime



def run():
    """Provides a list of all the towns, sorted by flood risk in descending order. 
    
    The towns are also given one of the four ratings:
    
    1. low
    2. moderate
    3. high
    4. severe """

    # Build a list of all the stations
    stations = build_station_list()

    # Update the water levels for all of them
    stationdata.update_water_levels(stations)

    towns_with_stations = geo.towns_with_stations(stations)

    # This will be a list of arrays (town, current level)
    towns_with_levels = []

    # Calculating the average current level for each town
    for i in towns_with_stations:
        levels_avg=0
        for s in i[1]:
            if s.relative_water_level():
                levels_avg+=s.relative_water_level()
        levels_avg/=len(i[1])
        towns_with_levels.append((i[0], levels_avg))

    # Sorting the list of towns by current water level
    towns_with_levels.sort(key=lambda a: a[1])

    # Create dictionary for risks in each town
    towns_with_risks = {}


    # Populating the dictionary with risk levels based on the current water level
    for i in towns_with_levels:
        if i[1]<1:
            towns_with_risks[i[0]]="low"
        elif i[1]<2.5:
            towns_with_risks[i[0]]="moderate"
        elif i[1]<3.5:
            towns_with_risks[i[0]]="high"
        else:
            towns_with_risks[i[0]]="severe"

    # Printing the risk level of each town based on the current water level
    for town, risk in towns_with_risks.items():
        print("Town: {:40} Risk: {}".format(town, risk))


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()