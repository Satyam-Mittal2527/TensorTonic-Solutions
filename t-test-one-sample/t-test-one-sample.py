import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    input_array = np.asarray(x, dtype = float)
    total_sum = np.sum(input_array)
    mean = np.mean(input_array)
    N = input_array.shape[0]
    X_mean = np.sum((input_array- mean)**2)
    s = np.sqrt(X_mean/(N-1))
    numerator = mean- mu0
    denominator = s/ np.sqrt(N)
    t = numerator/denominator
    return t
    pass