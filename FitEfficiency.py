# This is a comment. It doesn't get run as code. 

# Python uses "packages" of code that other people have written
# Use the import command to load those packages. 
import pandas
import numpy
import matplotlib
import scipy.interpolate
from numpy.polynomial import Polynomial as P
# Use the "pandas" package to read in the data file. 
data = pandas.read_csv("EfficiencyFiles/Rain_Water_Efficiency.csv",header=1, names=["E", "eff", "err1", "err2"])
# The header=1 tells pandas to use the first 2 lines as the names of the varaibles. 
# The names=["E", "eff", "err1", "err2"] tells pandas to overwrite those names with these ones. 

# This function returns a "data frame" where the columns are named. 
# show the contents of the data table
print("Data Frame:")
print(data)

# show only one column
print("E Column")
print(data["E"])

# access one element of the table
print("Element 3 of E is ",data["E"][2])


# To graph the data, we push it into the matplotlib.pyplot data structure. 
# The documentation for this command would be under pandas.DataFrame.plot()
data.plot(kind="scatter",x = "E", y = "eff");
#We will later use matplotlib.pyplot.show() to create the graphics. 

"""
# Polynomial fit
# in the includes, we defined P as numpy.polynomial.Polynomial
# deg is the degree of the polynomial. 
# domain tells the fit where to fit. 
fit = P.fit(data["E"], data["eff"], deg=2, domain=[0.5,3])
# to evaluate the function, use fit(x):
print fit(1)
# plot this fit
xx, yy = fit.linspace()
matplotlib.pyplot.plot(xx,yy)

matplotlib.pyplot.show()
"""


# Multiline comments in python go between three quaotation marks. 
# After you have played with the polynomial fits, comment out the polynomial section, and try using this interpolate section:

"""
# Linear Interpolation
lin = scipy.interpolate.interp1d(data["E"],data["eff"])
xxx = numpy.arange(min(data["E"]),max(data["E"]),0.05)
yyy = lin(xxx)
matplotlib.pyplot.plot(xxx,yyy)
print("Linear Interpolation of 1 is " + str(lin(1)))
matplotlib.pyplot.show()
"""

# Spline Fitting
# stitch together order 3 polynomials so they match the points and their derivatives are smooth
spline = scipy.interpolate.make_interp_spline(data["E"], data["eff"], k=3)
xxxx = numpy.arange(min(data["E"]), max(data["E"]), 0.05)
yyyy = spline(xxxx)
matplotlib.pyplot.plot(xxxx,yyyy)
print("Spline Interpolation of 1 is " + str(spline(1)))
matplotlib.pyplot.show()




