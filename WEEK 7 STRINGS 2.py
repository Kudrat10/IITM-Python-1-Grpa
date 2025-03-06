def has_a_in_second_half(s: str) -> bool:
    '''
    Given an even-length string, check if the second half contains 
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    '''
    # Get the second half of the string
    second_half = s[len(s)//2:]
    
    # Check if 'a' or 'A' is in the second half
    return 'a' in second_half or 'A' in second_half
