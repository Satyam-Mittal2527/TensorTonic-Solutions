import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.asarray(x)
    N = x.shape[0]
    mean = np.mean(x)
    print(mean)
    var = (np.sum((x-mean)**2))/(N-1)
    std = np.sqrt(var)
    return var,std
    pass