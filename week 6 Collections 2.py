def swap_alternate_elements(t):
    '''Swap every alternate of adjacent elements in the tuple.

    Args:
        t (tuple): A tuple of even length.

    Returns:
        tuple: A new tuple with alternate elements swapped.

    Examples:
    >>> swap_alternate_elements((1, 2, 3, 4, 5, 6))
    (2, 1, 4, 3, 6, 5)
    >>> swap_alternate_elements(('a', 'b', 'c', 'd'))
    ('b', 'a', 'd', 'c')
    '''
    # Convert the tuple to a list so that we can modify it
    lst = list(t)
    
    # Swap every adjacent pair of elements
    for i in range(0, len(lst), 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    
    # Convert the list back to a tuple and return
    return tuple(lst)
