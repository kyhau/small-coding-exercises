"""
Find longest sequence of zeros in binary representation of an integer.
See https://app.codility.com/programmers/lessons/1-iterations/binary_gap/.

Write an efficient algorithm for the following assumptions:
N is an integer within the range [1 .. 2,147,483,647 (or 2^31 - 1)].
"""
import logging
logging.basicConfig(level=logging.DEBUG)


# Convert decimal to binary with bin(), which returns result with prefix `0b`.
decimal_to_binary = lambda x : int(bin(x)[2:])


def solution(N):
    """
    Given a positive integer N, returns the length of its longest binary gap.
    The function returns 0 if N does not contain a binary gap.
    """
    binary_value = decimal_to_binary(N)
    logging.debug(f"Checking {N} ({binary_value})")

    # Strip all trailing 0s first, so the value of the first/last pos must be 1.
    stripped_value = str(binary_value).strip("0")

    max_gap = 0

    if stripped_value.count("0") > 0:
        start_pos = 0
        while 0 <= start_pos < len(stripped_value):
            end_pos = stripped_value.find("1", start_pos+1)
            max_gap = max(max_gap, end_pos-start_pos-1)
            start_pos = end_pos

    return max_gap
