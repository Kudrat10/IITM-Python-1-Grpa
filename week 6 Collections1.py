def rotate_list(lst: list, k: int) -> list:
    '''
    Given a list of items and an integer k, rotate the list to the right by k steps.

    Arguments:
    lst: list - a list of items
    k: int - the number of steps to rotate the list to the right

    Return:
    list - the rotated list
    '''
    # Handle the case where k is larger than the length of the list
    k = k % len(lst)
    
    # Slice the list and rearrange it
    return lst[-k:] + lst[:-k] if k != 0 else lst
