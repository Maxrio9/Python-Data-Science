from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt("daily_prices.csv", delimiter=",")

for i in range(0, 10):
  trash, pval = ttest_1samp(daily_prices[i], 1000)
  print(pval)