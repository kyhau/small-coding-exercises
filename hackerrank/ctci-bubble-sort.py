#!/bin/python3
"""
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
"""


# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0

    for i in range(len(a)):
        has_swapped = False

        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                has_swapped = True
        if has_swapped is False:
            break

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")