# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import numpy as np
import haversine

def stations_by_distance(stations, p):
    
    """The function stations_by_river creates a list of tuples with each station and its distance to a certain point p. The list is sorted by distance."""

    stations_new = []
    for s in stations:

        # distance can be computed using haversine library
        d=haversine.haversine(s.coord,p)
        stations_new.append((s, d))
    
    # list is sorted by the distance, which is the sevcond element in the tuples
    stations_new.sort(key=lambda a: a[1])

    return stations_new


def stations_within_radius(stations, centre, r):
    """The function stations_within_radius returns a list of the stations within a radius r from a centre"""
    
    stations_new=[]

    for s in stations:

        # distance can be computed using haversine library
        d=haversine.haversine(s.coord, centre)
        if d <= r:

            # if the station is within the radius, it is added to the list
            stations_new.append(s)

    return stations_new

def rivers_with_station(stations):
    """The function rivers_with_station returns a set of rivers which have an associated station."""
    # creates an array of rivers
    rivers = []

    # appends river into river list for each station
    for station in stations:
        rivers.append(station.river)
    
    # turns it into a set so that there are no repeats
    return set(rivers)

def stations_by_river(stations):

    """The function stations_by_river creates a dictonary whose keys are the names of rivers, and whose values are lists of stations on those rivers."""

    # creates a dictionary which maps river to station
    r_s_dict = {}
    for station in stations:

        # If this river has already been added o the dictionary, append the station name on 
        # the list that already exists
        if station.river in r_s_dict:
            r_s_dict[station.river].append(station.name)
        
        # Or, if the river has not yet been added to the dictionary, 
        # initialise the list of stations for that river and add to the dict
        else:
            stations_on_river = []
            stations_on_river.append(station.name)
            r_s_dict[station.river] = stations_on_river
    return r_s_dict

def rivers_by_station_number(stations, N):
    """This function returns the N number of rivers with the greatest number of stations."""  
    # creates dict which maps river to its stations
    r_s_dict = stations_by_river(stations)

    #creates the list which will hold the tuples of rivername, number of stations
    rivers = []
    
    #Iterates over all rivers, creating a tuple out of that river's name, and number of stations, 
    # and adding this to the rivers list
    for rivername, stations in r_s_dict.items():
        river_no_of_stations = rivername, len(stations)
        rivers.append(river_no_of_stations)
    
    #Sorts the rivers array by number of stations
    rivers.sort(key=lambda x:x[1])

    # create variable for the number of rivers, because this will save having to use len() function many times in the next loop
    no_of_rivers = len(rivers)
    # Initialise array which will contain the rivers with the N most stations, to be returned'
    rivers_moststations = []
    #Creates array of no of stations (not sure how to access solely number of stations other than in this way)
    station_numbers = [river[1] for river in rivers]
#all fine up to here
    for i in range(no_of_rivers - 1):
        
        # Creates a variable called index which will be the index referred to in the rivers list for this i
        index = no_of_rivers - 1 - i 
        #Appends the N biggest entries to the array     
        if index > (no_of_rivers - N - 1):
            rivers_moststations.append(rivers[index])
            continue
        
        # Adds river to list if number of stations of N+1th entry is equal to Nth entry, etc
        elif station_numbers[index] == station_numbers[index+1]:
            rivers_moststations.append(rivers[index])
            continue
        else:
            break

    return rivers_moststations

def towns_with_stations(stations):
    """This function returns a list of tuples of the format (town, [station1, station2, ....])
       The tuples contain the name of a town and then a list of all the stations near that town.
       The tuples are sorted alphabetically by town name."""

    # Couldn't sort the stations first by town because some of them had a null value.

    towns=[]

    # Populates the list with elements (town, [station])
    # second element in the tuple is a list because it will be extended later in towns2
    for s in stations:
        if s.town != None:
            towns.append((s.town,[s]))

    # Sorting the list by town names
    towns.sort(key=lambda a: a[0])

    # The list above still have more items for the same town. We will fix that now.
    towns2=[]

    # Populating the second list 
    for i in range(len(towns)):
        if i!=0:

            # If a sequence of items concerning the same town has ended, we add a new tuple element in towns2
            if towns[i][0] != towns[i-1][0]:
                towns2.append(towns[i])

            # If not, we add the station of the current item in towns (which is a repeating town) 
            # in the list inside the current element in towns2
            else:
                towns2[-1][1].append(towns[i][1][0])

        # We add the first entry in towns
        else:
            towns2.append(towns[i])

    return towns2
    # Note: I am very proud of this function.
    
