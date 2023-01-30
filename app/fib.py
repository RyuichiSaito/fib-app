import sympy


def fibonacci(n: int) -> int:
    """ Return the nth Fibonacci number

    Parameters
    ----------
    n : int
        The index of the Fibonacci number to return

    Returns
    -------
    int
        The nth Fibonacci number
    """
    # error handling
    if n < 0:
        raise ValueError("n must be >= 0")

    # calculate the nth Fibonacci number
    return int(sympy.fibonacci(n))
