"""This module contains a collection of functions related to flood risk."""
from floodsystem import station

def stations_level_over_threshold(stations,tol):
    """This function returns a list of tuples, where each tuple holds a station at which the latest relative water level is over tol and the relative water level at the station"""
    stations_over_threshold = []
    for station in stations:
        relative_level = station.relative_water_level()
        # If the relative level is smaller than the tolerance or equal to None (which means that the data is inconsistent), move on
        if relative_level == None:
            continue
        if relative_level <= tol:
            continue
        # If the relative level exceeds the tolerance, create the tuple contatining station and its level, and append the to the list
        elif relative_level > tol:
            t = station, relative_level
            stations_over_threshold.append(t)
            continue
    # Sorts the list by relative level, in descending order
    stations_over_threshold.sort(key = lambda x:x[1], reverse = True)
    return stations_over_threshold

def stations_highest_rel_level(stations,N):
    """This function returns a list of the N stations at which the water level, relative to the typical range, is highest."""
    # Using the above function, make a list of tuples containing station objects, and their levels, sorted in descending order. 
    # Note, tol is 0, so all_stations_with_level contains all of the stations
    all_stations_with_level = stations_level_over_threshold(stations, 0.0)
    return all_stations_with_level[:N]

