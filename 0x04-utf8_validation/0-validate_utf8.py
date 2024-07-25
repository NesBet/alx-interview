#!/usr/bin/python3
"""ValidUtf8 method"""


def validUTF8(data):
    """Determines if given data represents valid UTF-8 encoding.
    Args:
        data: A list of integers.
    Returns:
        True if valid UTF-8 encoding, otherwise False.
    """
    # No. of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7

    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6
    for num in data:

        # Get the number of set most significant bits.
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenes.
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If this byte is a part of an existing UTF-8 character, then we
            # simply have to look at the two most significant bits and we make
            # use of the masks we defined before.
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
