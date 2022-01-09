"""This module contains functions which can provide plots of the water levels. It includes the module analysis.py."""

import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime
from floodsystem import analysis



def plot_water_levels(station, dates, levels):
    """This function creates a plot of the water levels against the time for a specific station."""

    # Plot the levels against the timestamps
    plt.plot(dates, levels, label="Past level")

    # Plot the typical values as dashed lines
    level_low=station.typical_range[0]
    level_high=station.typical_range[1]
    plot_low, plot_high = [], []

    for i in dates:
        plot_low.append(level_low)
        plot_high.append(level_high)
    plt.plot(dates, plot_low, "--", label="Typical low")
    plt.plot(dates, plot_high, "--", label="Typical high")

    # Add all the labels and titles
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    # Show plot
    plt.tight_layout()
    plt.grid()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """This function creates a plot of the water levels against the time for a specific station.
       It also plots a best-fit polynomial curve for the water levels."""

    # Plot the levels against the timestamps
    plt.plot(dates, levels, label="Past level")

    # Plot the typical values as dashed lines
    level_low=station.typical_range[0]
    level_high=station.typical_range[1]
    plot_low, plot_high = [], []

    for i in dates:
        plot_low.append(level_low)
        plot_high.append(level_high)
    plt.plot(dates, plot_low, label="Typical low")
    plt.plot(dates, plot_high, label="Typical high")

    # Plot the best fit polynomial

    poly, d0 = analysis.polyfit(dates, levels, p)
    
    x=date2num(dates)
    plt.plot(x, poly(x-d0), "--", label = "Best fit")


    # Add all the labels and titles
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    # Show plot
    plt.tight_layout()
    plt.grid()
    plt.show()