import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    median = np.median(x)
    mean = np.mean(x)
    freq = Counter(x)
    mode = max(freq, key=freq.get)
    return mean,median,float(mode)
    pass