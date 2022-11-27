# Load libraries
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import numpy as np
import patsy

# Get some data
data = sm.datasets.get_rdataset('airquality').data
data.dropna(inplace=True)

# Fit model1 with sm
sm_model1 = sm.OLS.from_formula("Temp ~ Month + Day", data).fit()
print(sm_model1.params)
# Fit model1 with sklearn
X = data[["Month", "Day"]]
y = data[["Temp"]]
sk_model1 = LinearRegression()
sk_model1.fit(X, y)
print(sk_model1.intercept_)
print(sk_model1.coef_)
# Fit model2 with sm
sm_model2 = sm.OLS.from_formula("Temp ~ Month + Day + Month:Day + Ozone + np.power(Ozone, 2)", data).fit()
print(sm_model2.params)
# Fit model2 with sklearn

# data["MonthDay"] = data.Month * data.Day
# data["Ozone_sq"] = data.Ozone ** 2
# X = data[["Month", "Day", "MonthDay", "Ozone", "Ozone_sq"]]
# y = data[["Temp"]]
# Same results as the following line:
y, X = patsy.dmatrices('Temp ~ 0 + Month + Day + Month:Day + Ozone + np.power(Ozone, 2)', data)

sk_model2 = LinearRegression()
sk_model2.fit(X, y)
print(sk_model2.intercept_)
print(sk_model2.coef_)