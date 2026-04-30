def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    f_x = 2*a*x0 + b
    for i in range(steps):
        x0  = x0 - lr*f_x
        f_x = 2*a*x0 + b
        
    return x0
    # Write code here
    pass