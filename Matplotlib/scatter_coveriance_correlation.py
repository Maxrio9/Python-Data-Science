# Results in the png with the same name

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import pearsonr
np.set_printoptions(suppress=True, precision = 1) 

penguins = pd.read_csv('penguins.csv')
print(penguins.head())

plt.scatter(x = penguins.body_mass_g, y = penguins.flipper_length_mm)
plt.show()

covariance = np.cov(penguins.body_mass_g, penguins.flipper_length_mm)
print(covariance)
correlation, p = pearsonr(penguins.body_mass_g, penguins.flipper_length_mm)
print(correlation)