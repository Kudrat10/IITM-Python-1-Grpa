def unique_vowels(s: str) -> set:
    '''
    Given a string, return a set of unique vowels present in the string.

    Arguments:
    s: str - the input string

    Return:
    set - a set of unique vowels present in the string

    Examples:
    >>> unique_vowels('banana treat')
    {'a', 'e'}
    >>> unique_vowels('apple lolipop')
    {'a', 'e', 'i', 'o'}
    >>> unique_vowels('Ian Avinkov')
    {'I','A','a','i','o'}
    '''
    # Define the set of vowels (both lowercase and uppercase)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    # Initialize an empty set to store the unique vowels
    result = set()
    
    # Loop through each character in the string and check if it's a vowel
    for char in s:
        if char in vowels:
            result.add(char)
    
    return result
