def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    result = [x for x in tokens if x not in stopwords]
    return result
    pass