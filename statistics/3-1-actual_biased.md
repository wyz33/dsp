[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> To calculate the biased pmf for the number of children under 18 per family, we use the same method that was used in the class-size paradox:
If we base our calculation solely on surveys with the children, we would get a biased mean of 2.404 minors per family
However, if we calculate our mean based on the actual data based on the the NSFG survey, we get a mean of 1.024 minors per household.

If we further examine the two pmfs below we can see that when a family has no children, they are not represented at all in the biased pmf, whereas the number of families with 1 child is accurated represented in both pmfs (since the single child will not inflate the result), and the more children the family has, the more inflated the results in the biased pmf.
![pmf figure](wyz33.github.com/dsp/img/3-1-actual_biased_fig.png)

Below are the codes I used to get the results:
```
import thinkstats2
import thinkplot
#first get the data frame from the survey data
def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
   
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df
    

df = ReadFemResp()
data = df.numkdhh

#get the pmf from the data
real_pmf = thinkstats2.Pmf(data, label = 'actual')

#a function that takes the real pmf, and calculate the biased pmf
def biased_pmf(pmf, label):
    new_pmf  = pmf.Copy(label = label)
    for x, p in pmf.Items():
       new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

biased_pmf = biased_pmf(real_pmf, 'biased')

#plot both
thinkplot.Pmfs([real_pmf, biased_pmf])
thinkplot.Show(xlabel = 'number of children', ylabel= 'pmf')
#and display both means
print 'real mean is', real_pmf.Mean()
print 'biased mean is', biased_pmf.Mean()

```
