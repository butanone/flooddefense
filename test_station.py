# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    """This tests the typical_range_consistent method in the MonitoringStation class"""
    #Create a test station with consistent data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a test station with incomplete data
    q_id = "test-s-id"
    m_id1 = "test-m-id"
    label1 = "some station"
    coord1 = (-2.0, 4.0)
    trange1 = (None, 3.4445)
    river1 = "River X"
    town1 = "My Town"
    q = MonitoringStation(q_id, m_id1, label1, coord1, trange1, river1, town1)

    # Create a test station with inconsistent data
    r_id = "test-s-id"
    m_id2 = "test-m-id"
    label2 = "some station"
    coord2 = (-2.0, 4.0)
    trange2 = (None, 3.4445)
    river2 = "River X"
    town2 = "My Town"
    r = MonitoringStation(r_id, m_id2, label2, coord2, trange2, river2, town2)


    assert s.typical_range_consistent() == True
    assert q.typical_range_consistent() == False
    assert r.typical_range_consistent() == False
    
def test_inconsistent_typical_range_stations():
    """This tests the function inconsistent_typical_range_stations"""
    #Create a test station with consistent data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a test station with incomplete data
    q_id = "test-s-id"
    m_id1 = "test-m-id"
    label1 = "some station"
    coord1 = (-2.0, 4.0)
    trange1 = None
    river1 = "River X"
    town1 = "My Town"
    q = MonitoringStation(q_id, m_id1, label1, coord1, trange1, river1, town1)

    # Create a test station with inconsistent data
    r_id = "test-s-id"
    m_id2 = "test-m-id"
    label2 = "some station"
    coord2 = (-2.0, 4.0)
    trange2 = (4.0,3.0)
    river2 = "River X"
    town2 = "My Town"
    r = MonitoringStation(r_id, m_id2, label2, coord2, trange2, river2, town2)
    
    # perform the function on the list of custom made stations
    station_list = [s, q, r]
    inconsistentstations = inconsistent_typical_range_stations(station_list)
    assert q in inconsistentstations
    assert r in inconsistentstations
    assert s not in inconsistentstations

def test_relative_water_level():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2, 2)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 0

    q_id = "test-s-id"
    m_id1 = "test-m-id"
    label1 = "some station"
    coord1 = (-2.0, 4.0)
    trange1 = (-1.0, 2)
    river1 = "River X"
    town1 = "My Town"
    q = MonitoringStation(q_id, m_id1, label1, coord1, trange1, river1, town1)
    q.latest_level = -1.0
    
    assert s.relative_water_level() == 0.5
    assert q.relative_water_level() == 0