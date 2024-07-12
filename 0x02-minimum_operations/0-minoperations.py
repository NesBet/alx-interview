#!/usr/bin/python3
'''The minimum operations coding challenge.
'''

def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n 'H' characters.
    '''
    if not isinstance(n, int) or n <= 0:
        return 0
    
    ops_count = 0  # Counter for the number of operations
    clipboard = 0  # Clipboard to hold the current count of 'H'
    done = 1       # Current count of 'H' characters

    while done < n:
        if clipboard == 0:
            # Initial operation: copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2  # Two operations: copy + paste
        elif n - done > 0 and (n - done) % done == 0:
            # Copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2  # Two operations: copy + paste
        elif clipboard > 0:
            # Paste from clipboard
            done += clipboard
            ops_count += 1  # One operation: paste

    return ops_count
