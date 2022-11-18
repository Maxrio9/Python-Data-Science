from scipy.stats import iqr

dataset = [-50, -24, -13, -2, 0, 12, 15, 18, 73, 90, 10000]

dataset_range = max(dataset) - min(dataset)
dataset_iqr = iqr(dataset)

print("The range of the dataset is "+str(dataset_range))
print("The IQR of the dataset is "+str(dataset_iqr))