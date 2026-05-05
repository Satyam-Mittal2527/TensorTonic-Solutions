import numpy as np
def factorial(k):
    result =1
    for i in range (1,k+1):
        result = result * i
    return result 
def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    cdf = 0
    exp = np.exp(-lam)
    lambd = np.pow(lam,k)
    fact = factorial(k)
    print(fact)
    pmf = (exp*lambd)/fact
    for i in range(0,k+1):
        lambd = np.pow(lam,i)
        fact = factorial(i)
        cdf += (exp*lambd)/ fact
    return pmf, cdf
    pass