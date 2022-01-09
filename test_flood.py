"""Unit test for the flood module"""

from floodsystem import flood
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation


def test_stations_level_over_threshold():
    """Test the function stations_level_over_threshold"""
    stations = build_station_list()
    update_water_levels(stations)
    stations_over_threshold = flood.stations_level_over_threshold(stations, 5)
    for station in stations_over_threshold:
        # Tests that the relative level in the stations returned by stations_over_threshold is greater than the tolerance
        assert station[1] > 5

def test_stations_highest_rel_level():
    """Test the function stations_highest_rel_level"""
    stations = build_station_list()
    update_water_levels(stations)

    # create own station with a very high relative level, and check that this is in the highest_level_stations list
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0, 3)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 1000
    stations.append(s)
    highest_level_stations = flood.stations_highest_rel_level(stations,5)
    # test that the list returned is of correct length
    assert len(highest_level_stations) == 5
    # test that the highest level station is s, the custom station, and that the highest level is correct
    assert highest_level_stations[0] == (s, 1000/3)