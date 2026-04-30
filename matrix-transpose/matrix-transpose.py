import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code ]
    nparray = np.asarray(A)
    N,D = nparray.shape

    Transpose = np.zeros((D,N))
    
    for i in range(N):
        for j in range(D):
            Transpose[j,i] = A[i][j]

    return Transpose
    pass
