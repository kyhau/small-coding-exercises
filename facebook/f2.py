"""
https://www.careercup.com/question?id=5732335291465728
"""
import random

"""
Given an array of integers, randomly return an index of the maximum value
seen by so far.

E.g. Given [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]

Having iterated up to the at element index 5 (wher the last 30 is),
randomly gien an index among [1, 3, 4, 5] which are indices of 30
- the max value so far.
Each index should have 1/4 chance to get picked.

Having iterated through the entire array, randomly give an index between
8 and 9 which are indices of the max value 62.
"""
def func1(arr, selected_index):
    indices = []
    max_val = -1
    for i in range(min(selected_index+1, len(arr))):
        if arr[i] == max_val:
            indices.append(i)
        elif arr[i] > max_val:
            max_val = arr[i]
            indices = [i]
    return indices[random.randint(0, len(indices)-1)] if indices else -1


def test_func(test_data, test_case, expected):
    ret = func1(test_data, test_case)
    print(ret)
    assert ret in expected


test_data = [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]
for i in range(random.randint(0, 10)):
    test_func(test_data, 4, [1, 3, 4])
    test_func(test_data, 5, [1, 3, 4, 5])
    test_func(test_data, 9, [8, 9])
    test_func(test_data, 100, [8, 9])