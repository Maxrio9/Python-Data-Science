# Import libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')
print(lifespans.head())

vein_pack_lifespans = lifespans.lifespan[lifespans.pack == "vein"]
print("Average lifespan of a vein pack subscriber:", np.mean(vein_pack_lifespans))

trash, pval = ttest_1samp(vein_pack_lifespans, 73)
print(pval)

artery_pack_lifespans = lifespans.lifespan[lifespans.pack == "artery"]
print(np.mean(artery_pack_lifespans))

trash, pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(pval)


print(iron.head())
Xtab = pd.crosstab(iron.pack, iron.iron)
print(Xtab)

chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)