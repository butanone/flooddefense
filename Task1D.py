from floodsystem import geo
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""
    stations = build_station_list()
    #FIRST FUNCTION
    # all_rivers is a list of all rivers with a monitoring station. I used list because you can't sort a set
    all_rivers = list(geo.rivers_with_station(stations))

    # prints the number of rivers with at least 1 monitoring station
    print("Number of rivers with at least one monitoring station:", len(all_rivers))

    # prints the first 10 rivers, sorted alphabetically
    all_rivers.sort()
    print("First 10 rivers: ", all_rivers[:10])

    #SECOND FUNCTION
    # stations_by_river is the dict returned by the function
    stations_by_river = geo.stations_by_river(stations)

    # Prints the stations on required rivers
    print("Stations on River Aire: ", sorted(stations_by_river['River Aire']))
    print("Stations on River Cam: ", sorted(stations_by_river['River Cam']))
    print("Stations on River Thames: ", sorted(stations_by_river['River Thames']))





if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()