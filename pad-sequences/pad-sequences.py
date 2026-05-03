import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code
    maxlen = 0
    for sequeces in seqs:
        if len(sequeces) > maxlen:
            maxlen = len(sequeces)
            
    if max_len is None:
        max_len = maxlen
    print(max_len)
    result  = np.full([len(seqs), max_len], pad_value)
    for i,seqs in enumerate(seqs):
        length = len(seqs)
        if length > max_len:
            length= max_len
        print(length)
        result[i, :length] = seqs[:length]
    return result
    pass