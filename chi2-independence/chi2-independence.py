import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    input_array = np.array(C)
    row_sum = np.sum(input_array, axis=1)
    col_sum = np.sum(input_array, axis=0)
    print(row_sum)
    print(col_sum)
    total_sum = np.sum(input_array)
    N,D = input_array.shape
    Expected = np.zeros((N,D))
    for i in range(N):
        for j in range(D):
            expected = (row_sum[i]*col_sum[j])/ total_sum
            Expected[i,j] = expected
    chi_sqaure = np.sum(((input_array - Expected)**2)/Expected)
    return (chi_sqaure,Expected)
    pass