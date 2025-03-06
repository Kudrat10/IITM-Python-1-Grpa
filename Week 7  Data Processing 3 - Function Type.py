def find_longest_antakshari_subsequence(sequence: str) -> int:
    words = sequence.split(',')
    n = len(words)
    
    # Initialize variables to track the longest subsequence
    max_length = 1
    current_length = 1
    
    # Traverse through the words and check the antakshari property
    for i in range(1, n):
        if words[i-1][-1] == words[i][0]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    
    # Final check in case the longest subsequence ends at the last word
    max_length = max(max_length, current_length)
    
    return max_length


# Read input
n = int(input())  # The number of sequences
for _ in range(n):
    sequence = input().strip()  # A single sequence of words separated by commas
    result = find_longest_antakshari_subsequence(sequence)
    print(result)
