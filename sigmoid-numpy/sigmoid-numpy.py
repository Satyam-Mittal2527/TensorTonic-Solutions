import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    array = np.asarray(x, dtype=float)
    z = (1/ (1+ np.exp(-array)))

    return z
    pass