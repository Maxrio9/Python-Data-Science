# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# load data
heart = pd.read_csv('heart_disease.csv')

print(heart.head())

sns.boxplot(x = heart.heart_disease, y = heart.thalach)
plt.show()

thalach_hd = heart[heart.heart_disease == "presence"].thalach
thalach_no_hd = heart[heart.heart_disease == "absence"].thalach

print("Mean difference between HD thalach and non HD thalach:" , thalach_no_hd.mean() - thalach_hd.mean())
print("Median difference between HD thalach and non HD thalach:" , thalach_no_hd.median() - thalach_hd.median())

tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print(pval)
if (pval < 0.05):
  print("Value is significant \n")
else:
  print("Value is not significant \n")


plt.clf()
sns.boxplot(x = heart.heart_disease, y = heart.age)
plt.show()

age_hd = heart[heart.heart_disease == "presence"].age
age_no_hd = heart[heart.heart_disease == "absence"].age

print("Mean difference between HD age and non HD age:" , np.abs(age_no_hd.mean() - age_hd.mean()))
print("Median difference between HD thalach and non HD thalach:" , np.abs(age_no_hd.median() - age_hd.median()))

tstat, pval = ttest_ind(age_hd, age_no_hd)
print(pval)
if (pval < 0.05):
  print("Value is significant \n")
else:
  print("Value is not significant \n")


plt.clf()
sns.boxplot(x = heart.cp, y = heart.thalach)
plt.show()

thalach_typical = heart.thalach[heart.cp == "typical angina"]
thalach_asymptom = heart.thalach[heart.cp == "asymptomatic"]
thalach_nonangin = heart.thalach[heart.cp == "non-anginal pain"]
thalach_atypical = heart.thalach[heart.cp == "atypical angina"]

fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print("P-Value with ANOVA:", pval)

results = pairwise_tukeyhsd(endog = heart.thalach, groups = heart.cp)
print(results)

Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab, "\n")

chi2, pval, dof, expected = chi2_contingency(Xtab)
print("P-Value of Chi2 on CP and HD", pval)
if (pval < 0.05):
  print("Value is significant \n")
else:
  print("Value is not signifiant \n")