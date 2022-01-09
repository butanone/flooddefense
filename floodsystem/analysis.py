import numpy as np
from matplotlib.dates import date2num

def polyfit(dates, levels, p):
    """Given a list of levels and a list of corresponding dates, this function computes a best-fit polynomial.
       It returns a tuple of 2 elements: the np.poly1d object and a shift for the date axis."""

    # Convert the dates into floats
    x = date2num(dates)

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    # Return a tuple containing the polynomial object and the date shift
    return (poly, x[0])

def max_future_level(station, poly, shift, start, days):
   """This function returns the maximum relative level predicted for the next day by the best-fit polynomial curve."""

   start = date2num(start)
   # Array of times from present moment to one day later
   x = np.linspace(start, start+days, 100)

   # Array of predicted water levels
   y = poly(x-shift)

   # Finding maximum prediced level
   m=0
   for i in y:
      if i>m:
         m=i

   return m