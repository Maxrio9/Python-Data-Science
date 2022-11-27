import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

# Data from Kaggle: https://www.kaggle.com/datasets/nehatiwari03/harry-potter-fanfiction-data
hp = pd.read_csv('hp.csv')

# Try a scatter plot of two quantitative variables
sns.lmplot("follows", "favorites", data = hp)
plt.show()
plt.clf()

# Try the same plot colored by a binary variable
sns.lmplot("follows", "favorites", hue = "multiple", data = hp)
plt.show()
plt.clf()

# Try a model predicting a quantitative variable from two predictors
model0 = sm.OLS.from_formula("favorites ~ words + multiple", hp).fit()
print(model0.params)

# Try the same model but with an interaction term
model1 = sm.OLS.from_formula("favorites ~ words + multiple + words:multiple", hp).fit()
print(model1.params)

# Try a polynomial model
model2 =sm.OLS.from_formula("follows ~ words + np.power(words, 2)", hp).fit()
print(model2.params)
# Correlation is mostly linear therefore the squared term is very small

sns.lmplot(x = "follows", y = "words", data = hp, ci = False)
plt.plot(x = hp.favorites, y = model2.params[0] + model2.params[1] * hp.words + model2.params[2] * np.power(hp.words, 2))
plt.show()