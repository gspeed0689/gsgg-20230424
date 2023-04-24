def power(x, y):
    """Power function

    Args:
        x (int): integer
        y (int): integer
    """
    v = x
    for i in range(y):
        v = v * x
    return(v)