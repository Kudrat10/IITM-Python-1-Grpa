def number_of_unique_common_digits(n1: int, n2: int) -> int:
    '''
    Given two integers, return the number of unique digits that are common in both numbers.
    Eg, 287498,295424 - 2, 4 and 9 are common to both nums so answer is 3
    
    Arguments:
    n1: int - the first number
    n2: int - the second number

    Return:
    int - the number of unique common digits.
    '''
    # Convert both numbers to strings and extract unique digits using sets
    set_n1 = set(str(n1))
    set_n2 = set(str(n2))
    
    # Find the intersection of both sets (common digits)
    common_digits = set_n1 & set_n2
    
    # Return the number of common unique digits
    return len(common_digits)
