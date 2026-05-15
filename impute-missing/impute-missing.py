import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.array(X, dtype =float)
    value=0
    if strategy=='mean':
        value = np.nanmean(X, axis = 0, keepdims = True)
    elif strategy=='median':
        value = np.nanmedian(X, axis=0, keepdims = True)
    nanIdx = np.isnan(X)
    value = np.nan_to_num(value, nan=0)
    if X.ndim==1:
        X[nanIdx] = value
        return X
    X[nanIdx] = np.take(value, np.where(nanIdx)[1])
    return X
    pass