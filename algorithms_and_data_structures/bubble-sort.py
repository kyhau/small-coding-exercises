"""
Time:  Best/Average/Worst  O(n) / O(n^2) / O(n^2)
Space: O(1)
Stable, Adaptive, In-place: O(n) when nearly sorted
Good:
- Has many of the same properties as Insertion Sort, but has slightly overhead.
- In the case of nearly sorted data, takes O(n) time, but requires at least 2 passes through the data
  (whereas Insertion Sort requires something more like 1 pass).
Bad:  Inefficient on large lists
"""
import random


def bubble_sort(items):
    last_check_index = len(items)
    swapped = True
    while swapped:
        swapped = False
        for i in range(last_check_index-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        last_check_index -= 1


# Test
random_items = [random.randint(-50, 100) for c in range(32)]
print(f"Before: {random_items}")

bubble_sort(random_items)

print(f"After: {random_items}")
for i in range(len(random_items)-1):
    assert random_items[i] <= random_items[i+1]
