import numpy as np
from scipy.special import comb
def cal_pmf(n,p,k):
    num=1
    den = 1
    temp =n
    for i in range(k):
        num= num*temp
        temp= temp-1
    temp = k
    print(num)
    while(temp>=1):
        den = den*temp
        temp = temp-1
    pmf = (num/den) * np.pow(p,k) * np.pow(1-p,n-k)
    
    return pmf
def cal_cdf(n,p,k):
    sum=0
    for i in range(0,k+1):
        sum= sum+ cal_pmf(n,p,i)
    return sum
def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.

    """
    # Write code here
    pmf = cal_pmf(n,p,k)
    cdf = cal_cdf(n,p,k)
    return pmf,cdf
    pass