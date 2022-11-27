# import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

chol_hd = yes_hd.chol
print(chol_hd.mean())

trash, pvalue = ttest_1samp(chol_hd, 240)
pvalue = pvalue / 2
print(pvalue)
if (pvalue < 0.05):
  print("Value is significant")
else:
  print("Value is not significant")

chol_nhd = no_hd.chol
print("\n", chol_nhd.mean())

trash, pvalue = ttest_1samp(chol_nhd, 240)
pvalue = pvalue / 2
print(pvalue)
if (pvalue < 0.05):
  print("Value is significant")
else:
  print("Value is not significant")

num_patients = len(heart)
print("\n", num_patients)

num_highfbs_patients = np.sum(heart.fbs == 1)
print(num_highfbs_patients)

print("\n", np.round(num_patients * 0.08), "\n")

pvalue = binom_test(num_highfbs_patients, num_patients, 0.08)
print(pvalue)
if(pvalue < 0.05):
  print("Value is significant")
else:
  print("Value is not significant")