import numpy as np
print("1 Year better 1%:", 1 * np.power(1.01, 365))
print("1 Year better 2%:", 1 * np.power(1.02, 365))
print("2 Year better 1%:", 1 * np.power(1.01, (365 * 2)))
print("2 Year better 2%:", 1 * np.power(1.02, (365 * 2)))
print("3 Year better 1%:", 1 * np.power(1.01, (365 * 3)))
print("3 Year better 2%:", 1 * np.power(1.02, (365 * 3)))