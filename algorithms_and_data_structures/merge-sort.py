"""
Time: Best/Average/Worst: O(n log n)
Access: 0.5 * log n and log n comparisons per element, and between log n and 1.5 log n swaps per element
Space: O(n) extra space; for linked list can be implemented as O(1)
Stable, not adaptive

Can also be parallelized due to its divide-and-conquer nature
Does not require random access to data
Algorithm
- Top-down
- Bottom-up
Do exist in-place algorithm (complex and expensive)

Cache-aware versions of the merge sort algorithm (minimize the movement of pages in and out of a machine's memory
cache). For example, the tiled merge sort algorithm stops partitioning subarrays when subarrays of size S are reached,
where S is the number of data items fitting into a CPU's cache. Each of these subarrays is sorted with an in-place
sorting algorithm such as insertion sort, to discourage memory swaps.
"""
import operator
import random

compare=operator.lt


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if len(left) == i:
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    return result


def merge_sort(data):
    if len(data) < 2:
        return data[:]
    mid = len(data)//2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


# Test
random_items = [random.randint(-50, 100) for c in range(32)]
print(f"Before: {random_items}")

random_items = merge_sort(random_items)

print(f"After: {random_items}")
for i in range(len(random_items)-1):
    assert random_items[i] <= random_items[i+1]
