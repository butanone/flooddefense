# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """This method checks that the data provided for typical levels of the river are self-consistent and complete"""
        # if data provided is nonetype
        if self.typical_range == None: 
            return False
        # If tuple contains less than or more than two values
        elif len(self.typical_range) != 2:
            return False
        # If the low value provided is greater than the typical high value
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        else: 
            return True

    def relative_water_level(self):
        """This method  returns the latest water level as a fraction of the typical range"""
        # Return none if the latest level is unavailable or the data is inconsistent. This deals with inconsistent data
        if self.latest_level == None or self.typical_range_consistent == False:
            return None
        # If the data is consistent and complete, return the fraction as normal
        if self.typical_range_consistent() == True:
            return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])





def inconsistent_typical_range_stations(stations):
    """This function, given a list of station objects, returns a list of stations with inconsistent data"""
    # Initialise list which will contain inconsistent stations
    inconsistent_stations = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_stations.append(station)
    return inconsistent_stations
