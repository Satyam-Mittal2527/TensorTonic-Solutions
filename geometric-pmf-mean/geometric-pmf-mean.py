import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    in_arr = np.array(k)
    out_arr = np.pow(1-p,in_arr-1)*p
    e = 1/p
    return out_arr,e
    pass