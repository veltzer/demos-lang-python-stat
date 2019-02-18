# This example is taken from:
# https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables

# generate related variables
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
from numpy import cov
from scipy.stats import pearsonr
from scipy.stats import spearmanr

# seed random number generator
seed(1)

# prepare data
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)
# data2 = 10 * randn(1000) + 50

# summarize
print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))

# plot
pyplot.scatter(data1, data2)
pyplot.show()

# calculate covariance matrix
# cov(X, Y) = (sum (x - mean(X)) * (y - mean(Y))) * 1/(n-1)
covariance = cov(data1, data2)
print(covariance)

# calculate Pearson's correlation
# cov(X, Y) = (sum (x - mean(X)) * (y - mean(Y))) * 1/(n-1)
corr, _ = pearsonr(data1, data2)
print('Pearsons correlation: %.3f' % corr)

# calculate spearman's correlation
# Spearman's correlation coefficient = covariance(rank(X), rank(Y)) / (stdv(rank(X)) * stdv(rank(Y)))
corr, _ = spearmanr(data1, data2)
print('Spearmans correlation: %.3f' % corr)
