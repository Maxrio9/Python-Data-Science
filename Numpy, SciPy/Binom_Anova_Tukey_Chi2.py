# Import libraries
import numpy as np
import pandas as pd
import codecademylib3
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Import data
dogs = pd.read_csv('dog_data.csv')
print(dogs.head())

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]

whippet_rescues = dogs[dogs.breed == "whippet"]
num_whippet_rescues = np.sum(whippet_rescues.is_rescue == 1)
num_whippets = len(whippet_rescues)
print(num_whippet_rescues, num_whippets)

pval = binom_test(num_whippet_rescues, num_whippets, 0.08)
print(pval)

wt_whippets = dogs.weight[dogs.breed == "whippet"]
wt_terriers = dogs.weight[dogs.breed == "terrier"]
wt_pitbulls = dogs.weight[dogs.breed == "pitbull"]

fstat, pval = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print(pval)

results = pairwise_tukeyhsd(endog = dogs_wtp.weight, groups = dogs_wtp.breed)
print(results)

Xtab = pd.crosstab(dogs_ps.breed, dogs_ps.color)
print(Xtab)
chi2, pval, dof, expected = chi2_contingency(Xtab)
print(pval)