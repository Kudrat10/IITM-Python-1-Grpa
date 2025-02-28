def arithmetic_operations(t: tuple) -> tuple:
    '''
    Given a tuple of two integers (a, b), return a tuple containing the 
    sum, difference, product, and quotient (integer division) of the two numbers.

    Arguments:
    t: tuple - a tuple of two integers (a, b)

    Return:
    tuple - a tuple containing the sum, difference, product, and quotient

    Example:
    >>> arithmetic_operations((1, 2))
    (3, -1, 2, 0)
    '''
    a, b = t  # Unpack the tuple into a and b
    
    sum_result = a + b
    diff_result = a - b
    product_result = a * b
    quotient_result = a // b if b != 0 else 0  # Avoid division by zero

    return (sum_result, diff_result, product_result, quotient_result)
