# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head())
# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed, codecademy.score)
# Show then clear plot
plt.show()
plt.clf()
# Fit a linear regression to predict score based on prior lessons completed
result = sm.OLS.from_formula("score ~ completed", codecademy).fit()
print(result.params)
# Intercept interpretation:
# The expected score on the quiz if you haven't learned is 13.2
# Slope interpretation:
# For every completed task/lesson your score on the test improves by 1.3 points
# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed, codecademy.score)
plt.plot(codecademy.completed, result.params[0] + codecademy.completed * result.params[1])
# Show then clear plot
plt.show()
plt.clf()
# Predict score for learner who has completed 20 prior lessons
pred_20 = result.predict({"completed": 20})
print(pred_20)
# Calculate fitted values
fitted_values = result.predict(codecademy)
# Calculate residuals
residuals = codecademy.score - fitted_values
# Check normality assumption
plt.hist(residuals)
# Show then clear the plot
plt.show()
plt.clf()
# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)
# Show then clear the plot
plt.show()
plt.clf()
# Create a boxplot of score vs lesson
sns.boxplot(y = codecademy.score, x = codecademy.lesson)
# Show then clear plot
plt.show()
plt.clf()
# Fit a linear regression to predict score based on which lesson they took
result = sm.OLS.from_formula("score ~ lesson", codecademy).fit()
print(result.params)
# Calculate and print the group means and mean difference (for comparison)
mean_A = np.mean(codecademy.score[codecademy.lesson == "Lesson A"])
mean_B = np.mean(codecademy.score[codecademy.lesson == "Lesson B"])
print("Mean A:", mean_A)
print("Mean B:", mean_B)
print("Mean Difference:", np.abs(mean_A - mean_B))
# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x = "completed", y = "score", hue = "lesson", data = codecademy)
plt.show()