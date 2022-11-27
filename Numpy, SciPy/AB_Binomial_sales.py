# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, binom_test

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')
print(abdata.head())

Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)
chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)

num_visits = len(abdata)
print(num_visits)

num_sales_needed_099 = np.ceil(1000 / 0.99)
num_sales_needed_199 = np.ceil(1000 / 1.99)
num_sales_needed_499 = np.ceil(1000 / 4.99)
print(num_sales_needed_099, num_sales_needed_199, num_sales_needed_499)

p_sales_needed_099 = num_sales_needed_099 / num_visits
p_sales_needed_199 = num_sales_needed_199 / num_visits
p_sales_needed_499 = num_sales_needed_499 / num_visits
print(p_sales_needed_099, p_sales_needed_199, p_sales_needed_499)

samp_size_099 = len(abdata[abdata.group == "A"])
sales_099 = len(abdata[abdata.group == "A"][abdata.is_purchase == "Yes"])
print(samp_size_099, sales_099)
samp_size_199 = len(abdata[abdata.group == "B"])
sales_199 = len(abdata[abdata.group == "B"][abdata.is_purchase == "Yes"])
print(samp_size_199, sales_199)
samp_size_499 = len(abdata[abdata.group == "C"])
sales_499 = len(abdata[abdata.group == "C"][abdata.is_purchase == "Yes"])
print(samp_size_499, sales_499)

pvalueA = binom_test(sales_099, samp_size_099, p_sales_needed_099, alternative = "greater")
print(pvalueA)
pvalueB = binom_test(sales_199, samp_size_199, p_sales_needed_199, alternative = "greater")
print(pvalueB)
pvalueC = binom_test(sales_499, samp_size_499, p_sales_needed_499, alternative = "greater")
print(pvalueC)

# The price for the upgrade should be 4.99 $