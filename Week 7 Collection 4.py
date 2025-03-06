def final_position(pos: tuple, vel: tuple, time: int) -> tuple:
    '''
    Given an initial position of a point moving in a cartesian plane with a constant velocity, 
    find the final position of the point after a given time. 
    
    Hint: final position = initial position + velocity * time

    Args:
        pos - tuple[int]: A tuple representing the position vector (x1, y1).
        vel - tuple[int]: A tuple representing the velocity vector (vx, vy).
        time - int: Time of movement.

    Returns:
        tuple[int]: A tuple representing the final position (x, y).
    '''
    # Calculate the final position
    final_x = pos[0] + vel[0] * time
    final_y = pos[1] + vel[1] * time
    
    # Return the final position as a tuple
    return (final_x, final_y)
