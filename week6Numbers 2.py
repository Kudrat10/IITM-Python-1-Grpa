
def is_ten_digit_even(n):
    '''Checks if a number is a 10 digit even number.

    Also accounts for negative numbers by discarding the sign.

    Args: 
        n (int): The given number.
    
    Returns: 
        bool : result as True or False.
    
    Examples:
    >>> is_ten_digit_even(8769473839)
    False
    >>> is_ten_digit_even(928948)
    False
    >>> is_ten_digit_even(9289479278)
    True
    >>> is_ten_digit_even(-9289479278)
    True
    '''
    # Discard the sign if the number is negative
    n = abs(n)
    
    # Check if the number has exactly 10 digits
    if len(str(n)) == 10:
        # Check if the number is even
        return n % 2 == 0
    else:
        return False
