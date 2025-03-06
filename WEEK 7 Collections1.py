def reverse_first_half(t: tuple) -> tuple:
    '''
    Given an even-length tuple, return a new tuple where the first half 
    is reversed, and the second half remains unchanged.

    Arguments:
    t: tuple - an even-length tuple.

    Return: tuple - a new tuple with the first half reversed.
    '''
    # Get the first half and reverse it
    first_half = t[:len(t)//2][::-1]
    # Get the second half
    second_half = t[len(t)//2:]
    
    # Combine the reversed first half with the second half
    return first_half + second_half
