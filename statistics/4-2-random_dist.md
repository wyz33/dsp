[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> since by definition, random.random generates a number between 0 and 1 with equal probabilities, the PMF and CDF for 100 numbers picked with random.random should show uniform distribution.
If we look at the PMF and CDF generated, this is indeed the case. The PMF is 0.01 (1 out of 100) for all numbers picked, and the CDF is roughly a diagonal line (just like the percentile rank CDF), which is indicative of equal distribution of all the numbers.
If there is uneven distribution, we should see sharp rises in the CDF, but this is not the case.

![random figure](https://github.com/wyz33/dsp/blob/master/img/4-2-random.png)

Below is the code I used to generate the list of 100 numbers, as well as its PMF and CDF
```
import random
import thinkstats2
import thinkplot

x = []
for i in range(100):
    x.append(random.random())
    
x_pmf = thinkstats2.Pmf(x, label = "PMF")
x_cdf = thinkstats2.Cdf(x, label = "CDF")

thinkplot.PrePlot(2, rows = 2)
thinkplot.Pmf(x_pmf)

thinkplot.subplot(2)
thinkplot.Cdf(x_cdf)
```
