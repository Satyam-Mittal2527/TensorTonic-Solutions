import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))
def loss(y, pred, N):
    loss = np.sum(y*np.log(pred) + (1- y)*np.log(1-pred))
    loss = loss/N
    return loss
def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    N,D = X.shape
    w = np.zeros(D)
    b=0.0
    for epochs in range(steps):
        z = X @ w+ b
        pred = _sigmoid(z)

        dw = (1/N)*(X.T @ (pred - y))
        db = (1/N)*(np.sum(pred- y))

        w = w- lr*dw
        b = b - lr*db
        
    return w,b
    pass