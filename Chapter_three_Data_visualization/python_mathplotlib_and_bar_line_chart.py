# matplotlib.pyplot  module imported
from matplotlib import pyplot as plt

# data of years and gdp
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 542.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis 
plt.plot(years, gdp, color ='green', marker='o', linestyle='solid')

# add a title
plt.title("Normal GDP")

# add a lable to the y-axis
plt.ylabel("Billins of $")
plt.show()
