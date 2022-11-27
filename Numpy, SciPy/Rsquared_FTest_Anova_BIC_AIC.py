import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

# Import data
rentals = pd.read_csv('rentals.csv')

# Explore and test out models below:
model1 = sm.OLS.from_formula("rent ~ size_sqft + building_age_yrs + has_washer_dryer + has_elevator", rentals).fit()
model2 = sm.OLS.from_formula("rent ~ size_sqft + min_to_subway + has_gym + has_elevator + borough", rentals).fit()

print(model1.rsquared_adj, model2.rsquared_adj)
print("Model 2 is better in the adjusted R-squared statistic")

anova_result = anova_lm(model1, model2)
print(anova_result)
print("Model 2 is significantly better according to the F-test")

print(model1.aic, model2.aic)
print("Model 2 is better according to the AIC statistic")

print(model1.bic, model2.bic)
print("Model 2 is better according to the AIC statistic")

print("The test have unanimously choosen Model 2 as the better predictor")