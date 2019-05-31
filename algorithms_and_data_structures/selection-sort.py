"""
Time: 	Best/Average/Worst	O(n^2)	runtime is always quadratic.
Space: 	O(1) extra space
Swaps:	O(n)
Stable, not adaptive, In-place
Algorithm:
  - Find the smallest (or largest) item and put in to the left (from leftmost to rightmost)
Good:
  - Simple, performance advantage over more complicated algorithms where auxiliary memory is limited.
  - Has the property of minimising number of swaps; good in applications where the cost of swapping items is high.
Bad:
  - Inefficient on large lists
  - Generally performs worse than Insertion Sort.
"""
import random


def selection_sort(items):
    for i in range(0, len(items)):
        smallest_index = i
        for k in range(i+1, len(items)):
            if items[smallest_index] > items[k]:
                smallest_index = k
        if smallest_index != i:
            items[smallest_index], items[i] = items[i], items[smallest_index]


# Test
random_items = [random.randint(-50, 100) for c in range(32)]
print(f"Before: {random_items}")

selection_sort(random_items)

print(f"After: {random_items}")
for i in range(len(random_items)-1):
    assert random_items[i] <= random_items[i+1]
