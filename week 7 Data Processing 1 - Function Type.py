def row_index_with_most_number_of_zeros(matrix: list) -> int:
    '''
    Given a matrix, find the index of the row with the 
    maximum number of zeros in it.

    Arguments: 
    matrix: list[list] - A 2D list representing the matrix.

    Returns: 
    int - The index of the row with the maximum number of zeros.
    '''
    max_zeros = -1  # To track the maximum number of zeros encountered
    max_index = -1  # To track the index of the row with the maximum number of zeros

    # Iterate over each row in the matrix
    for i, row in enumerate(matrix):
        zero_count = row.count(0)  # Count the zeros in the current row
        
        # Update if this row has more zeros
        if zero_count > max_zeros:
            max_zeros = zero_count
            max_index = i

    return max_index
