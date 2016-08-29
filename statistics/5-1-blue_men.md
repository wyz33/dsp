[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> To find out the percent of men in the US that would be qualified for the Blue Man Group based on their height requirements, we just need to find the percentile for the minimum and maximum allowed heights.
The percent qualified would be the difference between the minimum and maximum percentile.
Based on the results of this particular survey, 34.3 percent of men in the US would qualify for the Blue Man Group.

The figure below illustrates how we arrived at this answer:
The curve is the CDF of the analytical distribution of men's heights in the US ( with mean = 178.0cm and standard deviation = 7.7cm)
The vertical lines point out the minimum and maximum allowed heights for the Blue Man Group, the horizontal lines indicates their corresponding percentiles. The percent of the population that would qualify for the group is the difference of the two horizontal levels.
![pmf figure](https://github.com/wyz33/dsp/blob/master/img/5-1-blueman.png)

See below for my code for this exercise
```
import scipy
import numpy as np
import matplotlib.pyplot as plt


def allft(ft, inch):
    new = ft + inch/12.0
    return new

def ft2cm(ft):
    new = ft*30.48
    return new
    
mu = 178.0
sigma = 7.7

min_ft = 5
min_inch = 10
min_ht_ft = allft(min_ft, min_inch)
max_ft = 6
max_inch = 1
max_ht_ft = allft(max_ft, max_inch)

min_cm = ft2cm(min_ht_ft)
max_cm = ft2cm(max_ht_ft)

percentile_max = scipy.stats.norm.cdf(max_cm, loc = mu, scale = sigma)
percentile_min = scipy.stats.norm.cdf(min_cm, loc = mu, scale = sigma)

percent_qualified = percentile_max - percentile_min

print percent_qualified*100, 'percent of men in the US would qualify for the Blue Man Group.'

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(140, 220, 0.1)
# Mean = 0, SD = 2.
fig = plt.figure()
plt.plot(x_axis, scipy.stats.norm.cdf(x_axis,mu,sigma))

plt.plot([140, 220], [percentile_max, percentile_max])
plt.plot([140, 220], [percentile_min, percentile_min])
plt.plot([min_cm, min_cm], [0, 1])
plt.plot([max_cm, max_cm], [0, 1])

plt.xlabel('height in cm')
plt.ylabel('CDF')
```
