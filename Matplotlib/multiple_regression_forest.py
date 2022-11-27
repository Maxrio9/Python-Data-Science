#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

#load data
# Data origin: https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++
'''
Data contains:
temp – maximum temperature in degrees Celsius
humid – relative humidity as a percentage
region – location in Bejaia in the northeast of Algeria or Sidi Bel-abbes in the northwest of Algeria
fire – whether a fire occurred (True) or didn’t (False)
FFMC – Fine Fuel Moisture Code: measure of forest litter fuel moisture that incorporates temperature, humidity, wind, and rain
ISI – Initial Spread Index: estimates spread potential of fire
BUI – Buildup Index: estimates potential release of heat
FWI – Fire Weather Index: measure of general fire intensity potential that incorporates ISI and BUI
'''

forests = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00547/Algerian_forest_fires_dataset_UPDATE.csv')

#check multicollinearity with a heatmap
corr_grid = forests.corr()
sns.heatmap(corr_grid)
plt.show()
plt.clf()
# Higly correlated predictors: DMC & DC, DMC & BUI, DMC & FWI, FWI & ISI

#plot humidity vs temperature
sns.lmplot(x = "temp", y = "humid", hue = "region", data = forests)
plt.show()
plt.clf()

#model predicting humidity
modelH = sm.OLS.from_formula("humid ~ temp + region", forests).fit()
print(modelH.params)

#equations
# humid = 142.58 - 7.25 * region - 2.39 * temp
# Bejaia = 142.58 - 2.39 * temp
# Sidi Bel-abbes = 135.33 + 2.39 * temp

#interpretations
## Coefficient on temp:
# The Coefficient means that on average for every degree of temperature the humidity is lower by 2.4%
## For Bejaia equation:
# The intercept does not really make sense as the humidity can't be above 100, but limiting the Line to a humidity between 100 and 0 would make sense
## For Sidi Bel-abbes equation:
# The same as in the Bejaia region applies

#plot regression lines
sns.lmplot("temp", "humid", hue = "region", data = forests, ci = False, fit_reg = False)
plt.plot(forests.temp, modelH.params[0] + modelH.params[2] * forests.temp, linewidth = 3, label = "Bejaia", color='blue')
plt.plot(forests.temp, modelH.params[0] + modelH.params[1] + modelH.params[2] * forests.temp, linewidth = 3, label = "Sidi Bel-abbes", color = "orange")
plt.legend()
plt.show()
plt.clf()

#plot FFMC vs temperature
sns.lmplot("temp", "FFMC", hue = "fire", data = forests)
plt.show()
plt.clf()

#model predicting FFMC with interaction
resultsF = sm.OLS.from_formula("FFMC ~ temp + fire + temp:fire", forests).fit()
print(resultsF.params)

#equations
## Full equation:
# FFMC = -8.11 + fire * 76.79 + temp * 2.45 + temp * fire * -1.89
## For locations without fire:
# FFMC = -8.11 + temp * 2.45
## For locations with fire:
# FFMC = 68.68 + temp * 0.56

#interpretations
## For locations without fire:
# The chance of fire starts out really low and is strongly affected by the temperature
## For locations with fire:
# The chance of fire starts out high and is weakly affected by the temperature

#plot regression lines
sns.lmplot("temp", "FFMC", hue = "fire", data = forests, fit_reg = False)
plt.plot(forests.temp, resultsF.params[0] + forests.temp * resultsF.params[2], linewidth = 3, label = "No Fire")
plt.plot(forests.temp, resultsF.params[0] + resultsF.params[1] + forests.temp * resultsF.params[2] + forests.temp * resultsF.params[3], linewidth = 3, label = "Fire")
plt.legend()
plt.show()
plt.clf()


#plot FFMC vs humid
sns.lmplot("humid", "FFMC", forests, fit_reg = False)
plt.show()
plt.clf()

#polynomial model predicting FFMC
resultsP = sm.OLS.from_formula("FFMC ~ humid + np.power(humid, 2)", forests).fit()
print(resultsP.params)

#regression equation
# FFMC = resultsP.params[0] + forests.humid * resultsP.params[1] + resultsP.params[2] * np.power(forests.humid, 2)

#sample predicted values
FFMC_25 = resultsP.params[0] + 25 * resultsP.params[1] + resultsP.params[2] * np.power(25, 2)
FFMC_35 = resultsP.params[0] + 35 * resultsP.params[1] + resultsP.params[2] * np.power(35, 2)
FFMC_60 = resultsP.params[0] + 60 * resultsP.params[1] + resultsP.params[2] * np.power(60, 2)
FFMC_70 = resultsP.params[0] + 70 * resultsP.params[1] + resultsP.params[2] * np.power(70, 2)
print(FFMC_25, FFMC_35)
print(FFMC_60, FFMC_70)

#interpretation of relationship
# The FFMC starts out with a high value of 77.6 and rises, until it reaches a tipping point where the values start to decline exponentialy

#multiple variables to predict FFMC
modelMV = sm.OLS.from_formula("FFMC ~ humid + temp + wind + rain", forests).fit()
print(modelMV.params)

#predict FWI from ISI and BUI
modelFWI = sm.OLS.from_formula('FWI ~ ISI + BUI',data=forests).fit()
print(modelFWI.params)