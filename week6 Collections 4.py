def common_char_sorted_str(s1: str, s2: str) -> str: 
    '''Returns a sorted string with unique common characters present in the given strings.

    Arg:
        s1 (str) : Input string. 
        s2 (str) : Input string. 

    Returns: 
        str: string of unique common characters arranged in ascending order. 

    Examples:
    >>> common_char_sorted_str('apple', 'ball')
    'al'
    >>> common_char_sorted_str('abcde', 'edfci')
    'cde'
    '''
    # Convert strings to sets to remove duplicates and find common characters
    common_chars = set(s1) & set(s2)
    
    # Sort the common characters and join them into a string
    return ''.join(sorted(common_chars))

