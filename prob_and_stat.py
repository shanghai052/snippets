#!/usr/bin/env python
import math

mean = lambda nums: sum(nums) / float(len(nums))
vary = lambda nums: sum([x**2 for x in nums])/len(nums) - sum(nums)**2/float(len(nums))**2
std_dev = lambda nums: math.sqrt(vary(nums))
std_score = lambda x, nums: (x - mean(nums)) / std_dev(nums)
low_qrt = lambda nums: (math.ceil(len(nums)/2.0) / 2) - 1
up_qrt = lambda nums: (math.ceil(len(nums)/2.0)) + (math.ceil(len(nums)/2.0)) / 2 - 1
median = lambda nums: (math.ceil(len(nums)/2.0))
binomial = lambda n, k: math.factorial(n) / (math.factorial(n-k) * math.factorial(k))
bin_dist = lambda p, n, k: (math.factorial(n) / (math.factorial(n-k) * math.factorial(k))) * p**k * (1 - p)**(n-k)

x = [33,17,13]
#[-99, 13,17,33,1489]

print 'mean', mean(x)
print 'variance', vary(x)
print 'standard deviation', std_dev(x)
print 'standard score', std_score(5, x)
print 'lower quartile', x[int(low_qrt(x))], low_qrt(x)
print 'median', x[int(median(x))], median(x)
print 'upper quartile', x[int(up_qrt(x))], up_qrt(x)
print 'adjusted mean', mean(x[int(low_qrt(x)):int(up_qrt(x))])
print 'binomial', binomial(3, 3)
print 'binomial distribution', bin_dist(0.8, 12, 9)
