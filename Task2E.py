from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem import flood, plot, stationdata
import datetime


def run():
    """Plots the water level over the past 10 days for the 5 stations at which the current relative water level is greatest."""
    
    # Build a list of all the stations
    stations = build_station_list()

    # Update the water levels for all of them
    update_water_levels(stations)

    # Find which are the 5 stations with highest relative level
    high_risk_stations = flood.stations_highest_rel_level(stations,5)

    days = 10
    dates, levels = [], []

    # Plot the water levels
    for st in high_risk_stations:
        dates, levels = fetch_measure_levels(st[0].measure_id, dt=datetime.timedelta(days=days))
        plot.plot_water_levels(st[0], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()