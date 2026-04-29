import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    x =  x - np.max(x, axis=-1, keepdims=True) 
    num = np.exp(x)
    den = np.sum(num, axis=-1, keepdims = True)

    z = num/den
    return z
    pass