import codecademylib3
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

family = pd.read_csv('family.csv')

#create heat map here:
corr = family.corr()
sns.heatmap(corr)
plt.show()
plt.clf()
#Rice and Bread correlate strongly ~ 0.9

#fit model and view summary here:
results = sm.OLS.from_formula("income ~ food + housing + source", family).fit()
print(results.params)

#write out regression equation here:
#y = b0 + b1 * x + b2 * x + b3 * x +....

#interpret intercept here:
# The average income for people who don't have food or housing and source their income by activities is -26.8

#interpret the coefficient on source here:
# For income source of Wage/Salaries the average goes up by 29.7 and for Entrepreneurship another 29.7

#interpret the coefficient on food here:
# For every unit of food they have their income goes up by 1.5

#interpret the coefficient on housing here:
# For every unit of housing they have their income goes up by 3.2

#plot regression lines on scatter plot here:
sns.lmplot(x = "housing", y = "income", hue = "source", data = family)
plt.plot(family.housing, results.params[0]+results.params[1]*1+results.params[3]*family.housing+results.params[2]*10, color='red',linewidth=5, label='food=10')
plt.plot(family.housing, results.params[0]+results.params[1]*1+results.params[3]*family.housing+results.params[2]*100, color='orange',linewidth=5, label='food=100')
plt.plot(family.housing, results.params[0]+results.params[1]*1+results.params[3]*family.housing+results.params[2]*200, color='yellow',linewidth=5, label='food=200')
plt.legend()

plt.show()