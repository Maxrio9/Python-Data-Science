# Results can be seen in the PNG with the same name

import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)
plt.hist(in_bloom, range=(0, 365), bins = 365)

plt.title("Flowers blooming per day")
plt.xlabel("Day of the Year")
plt.ylabel("Number of Flowers blooming")

plt.subplot(212)
plt.hist(flights, range=(0, 365), bins = 365)

plt.title("Flights every day")
plt.xlabel("Day of the Year")
plt.ylabel("Number of Flights")

plt.tight_layout()
plt.show()