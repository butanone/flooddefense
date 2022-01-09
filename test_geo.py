"""test for the geo module"""

from floodsystem import geo
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation


def test_stations_by_distance():
    """Test the function stations_by_distance"""
    
    # Build the stations list
    stations=build_station_list
    cam=(52.2053, 0.1218)
    stations_new=geo.stations_by_distance(stations,cam)

    # Test that there are entries
    assert len(stations_new) != 0

    # Test the first and last entries
    assert stations_new[0][0]  == 'Cambridge Jesus Lock'
    assert stations_new[-1][0] == 'Penberth'


def test_stations_within_radius():
    """Test the function rivers_with_station"""

    # Build the stations list
    stations = build_station_list()
    cam=(52.2053, 0.1218)

    # Test 0 results for radius 0
    stations_new=geo.stations_within_radius(stations,cam, 0)
    assert len(stations_new) == 0

    # Test results include all stations for a huge radius
    stations_new=geo.stations_within_radius(stations,cam, 10000)
    assert len(stations_new) == len(stations)


def test_rivers_with_station():
    """Test the function rivers_with_station"""
    stations = build_station_list()
    x = geo.rivers_with_station(stations)

    # Search for river cam
    for river in x:
        if river == 'River Cam':
            river_cam = river
    
    # Test that there are entries
    assert len(x) != 0
    # Test that river cam is found
    assert river_cam

def test_stations_by_river():
    """Test the function stations_by_river"""
    stations = build_station_list()
    x = geo.stations_by_river(stations)
    # Test that there are entries
    assert len(x) != 0
    
    # Create a list of station consisting of my_station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    my_station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    my_station_list = []
    my_station_list.append(my_station)
    my_station_by_river = geo.stations_by_river(my_station_list)

    # Test that the key "River X" has been added
    assert "River X" in my_station_by_river
    

def test_rivers_by_station_number():
    """Test the function rivers_by_station_number"""
    stations = build_station_list()
    x = geo.rivers_by_station_number(stations, 8)

    # Checks that output is of right length
    assert len(x) == 8

    