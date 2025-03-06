def seconds_to_minute_seconds(seconds: int) -> tuple:
    '''
    Given an integer representing seconds, return a tuple of (minutes, seconds).

    Arguments:
    seconds: int - an integer representing the number of seconds.

    Return: tuple - a tuple of (minutes, remaining_seconds).
    '''
    minutes = seconds // 60  # Get the number of full minutes
    remaining_seconds = seconds % 60  # Get the remaining seconds
    return (minutes, remaining_seconds)
