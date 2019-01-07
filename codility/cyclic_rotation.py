"""
Rotate an array to the right by a given number of steps.
See https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/.

An array A consisting of N integers is given. Rotation of the array means that each element is shifted right
by one index, and the last element of the array is moved to the first place.
For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one
index and 6 is moved to the first place).
The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Assume that
- N and K are integers within the range [0..100];
- each element of array A is an integer within the range [-1000 .. 1000]
"""


def solution(A, K):
    """
    Given an array A consisting of N integers and an integer K, returns the array A rotated K times.
    """
    for i in range(K):
        A.insert(0, A.pop())

    return A

