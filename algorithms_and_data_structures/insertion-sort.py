"""
Time: 	Best/Average/Worst	O(n) / O(n^2) / O(n^2)
Space: 	O(1) extra space
Swaps: 	O(n^2)
Stable,Adaptive, In-place: O(n) when nearly sorted
Algorithm:
  Iterate from leftmost to rightmost, for each element, compare backward one by one to the leftmost and swap with an
  element if it is smaller than that element.
Good:
  Simple implementation
  It is adaptive, good when data is nearly sorted, or the problem size is small (because it has low overhead).
  It is often used as the recursive base case (when the problem size is small) for higher overhead divide-and-conquer
  sorting algorithms (e.g. merge sort, quick sort).
Bad:  Inefficient on large lists.
"""
import random


def insertion_sort(items):
    for i in range(1, len(items)):
        for k in range(i, 0, -1):
            if items[k-1] <= items[k]:
                break
            items[k-1], items[k] = items[k], items[k-1]


# Test
random_items = [random.randint(-50, 100) for c in range(32)]
print(f"Before: {random_items}")

insertion_sort(random_items)

print(f"After: {random_items}")
for i in range(len(random_items)-1):
    assert random_items[i] <= random_items[i+1]
