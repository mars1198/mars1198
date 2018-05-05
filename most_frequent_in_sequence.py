def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    return max(set(data), key=data.count)
