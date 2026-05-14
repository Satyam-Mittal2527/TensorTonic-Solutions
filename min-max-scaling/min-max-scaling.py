import numpy as np

def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    data = np.asarray(data, dtype=float)
    min  = np.min(data, axis=0, keepdims = True)
    max = np.max(data, axis =0, keepdims = True)
    den = max-min
    output = (data- min)/ np.maximum(den, 1e-3)

    return output.tolist()