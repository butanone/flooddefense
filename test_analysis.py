from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem import analysis
from floodsystem import flood
import datetime
"""Unit test for the analysis module"""

def test_polyfit():
    """Unit test for the polyfit function"""
    stations = build_station_list()

    # Update the water levels for all of them
    update_water_levels(stations)

    # Find which are the 5 stations with highest relative level
    high_risk_stations = flood.stations_highest_rel_level(stations,1)

    days = 2
    dates, levels = [], []

    # Add dates and levels to the lists
    for st in high_risk_stations:
        dates, levels = fetch_measure_levels(st[0].measure_id, dt=datetime.timedelta(days=days))
    
    test_array = analysis.polyfit(dates, levels, 3)
    # test that polyfit returns a polynomial of the correct order
    assert len(test_array[0])== 3
