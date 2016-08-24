[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The mean birth weight of first born babies is : 7.20lbs, and that for the other babies is 7.33 lbs. The Cohen's D is -0.0887 pooled standard deviations. While the difference is slightly larger than the pregnancy length between first vs other babies, it is still quite small.

I used most of the pandas Series computation to calcuate the mean, variance, and the standard deviation of the birth weights of the two groups. I did write my own code for calcuating the Cohen's d.

```
import math
import numpy as np

import nsfg
import thinkstats2
import thinkplot

pregdf = nsfg.ReadFemPreg()
live_birth = pregdf[pregdf.outcome == 1]
first = live_birth[live_birth.birthord ==1]
others = live_birth[live_birth.birthord !=1]

firstbwmean = first.totalwgt_lb.mean()
firstbwvar = first.totalwgt_lb.var()
firstbwstd = first.totalwgt_lb.std()

othersbwmean = others.totalwgt_lb.mean()
othersbwvar = others.totalwgt_lb.var()
othersbwstd = others.totalwgt_lb.std()

nfirst = len(first)
nothers = len(others)
pooled_var = (firstbwvar*nfirst + othersbwvar*nothers)/(nfirst+nothers)

Cohensd= (firstbwmean-othersbwmean)/math.sqrt(pooled_var)

print Cohensd
```
