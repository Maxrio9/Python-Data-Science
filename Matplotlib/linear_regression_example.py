# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
website = pd.read_csv('website.csv')

# Print the first five rows
print(website.head())

# Create a scatter plot of time vs age
plt.scatter(x = website.age, y = website.time_seconds)

# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict time_seconds based on age
model = sm.OLS.from_formula("time_seconds ~ age", website)
result = model.fit()
print(result.params)

# Plot the scatter plot with the line on top
plt.scatter(website.age, website.time_seconds)
plt.plot(website.age, result.params[0] + result.params[1]*website.age)

# Show then clear plot
plt.show()
plt.clf()

# Calculate fitted values
fitted_values = result.predict(website)
print(fitted_values.head())

# Calculate residuals
residuals = fitted_values - website.time_seconds
print(residuals.head())

# Check normality assumption
plt.hist(residuals)
# normaly distributed

# Show then clear the plot
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(residuals, fitted_values)
# homoscedastic

# Show then clear the plot
plt.show()
plt.clf()

# Predict amount of time on website for 40 year old
pred_40 = result.predict({"age": 40})
print(pred_40)

# Fit a linear regression to predict time_seconds based on the browser
model = sm.OLS.from_formula("time_seconds ~ browser", website)
result = model.fit()
print(result.params)

# Calculate and print the group means (for comparison)
print("Safari Mean:", np.mean(website.time_seconds[website.browser == "Safari"]))
print("Chrome Mean:", np.mean(website.time_seconds[website.browser == "Chrome"]))