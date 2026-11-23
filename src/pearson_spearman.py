"""
This example is taken from:
https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables
"""

import numpy as np
from matplotlib import pyplot as plt
from numpy import cov, mean, std
from scipy.stats import pearsonr, spearmanr

# seed random number generator
rng = np.random.default_rng(1)

# prepare data
data1 = 20 * rng.standard_normal(1000) + 100
data2 = data1 + (10 * rng.standard_normal(1000) + 50)
# data2 = 10 * rng.standard_normal(1000) + 50

# summarize
print(f"data1: mean={mean(data1)} stdv={std(data1)}")
print(f"data2: mean={mean(data2)} stdv={std(data2)}")

# plot
plt.scatter(data1, data2)
plt.show()

# calculate covariance matrix
# cov(X, Y) = (sum (x - mean(X)) * (y - mean(Y))) * 1/(n-1)
covariance = cov(data1, data2)
print(covariance)

# calculate Pearson's correlation
# cov(X, Y) = (sum (x - mean(X)) * (y - mean(Y))) * 1/(n-1)
corr, _ = pearsonr(data1, data2)
print(f"Pearsons correlation: {corr}")

# calculate spearman's correlation
# Spearman's correlation coefficient =
# covariance(rank(X), rank(Y)) / (stdv(rank(X)) * stdv(rank(Y)))
corr, _ = spearmanr(data1, data2)
print(f"Spearmans correlation: {corr}")
