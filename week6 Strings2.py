def even_first_odd_reversed(s: str) -> str:
    '''Return a string with the characters in the even indices first 
    and the characters in the odd indices reversed next.

    Arguments:
    s: str - the input string

    Return:
    str - modified string

    Example:
    >>> even_first_odd_reversed('abcde')
    'acedb'
    >>> even_first_odd_reversed('python')
    'ptonhy'
    '''
    # Extract even indexed characters
    even_chars = s[::2]
    
    # Extract odd indexed characters and reverse them
    odd_chars = s[1::2][::-1]
    
    # Combine even_chars and reversed odd_chars
    return even_chars + odd_chars
