import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=float)
    N = y_pred.shape[0]
    correctprob=  y_pred[np.arange(N), y_true]

    loss = -np.mean(np.log(correctprob))

    return loss
    pass