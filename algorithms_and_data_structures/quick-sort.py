"""
Time: Best/Average/Worst: O(n log n) / O(n log n) / O(n^2)
Most implementations are unstable, as stable in-place partitioning is more complex.
Quicksort can also be parallelized due to its divide-and-conquer nature (if not using in-place partition).
Quicksort can be implemented with an in-place partitioning algorithm, so the entire sort can be done with only O(log n)
additional space used by the stack during the recursion.
Good:
- Quicksort is often faster in practice than other O(n log n) algorithms.
- Quicksort's sequential and localized memory references work well with a cache.
Bad:
- O(n^2) in the worst case, though this behaviour is rare, but is unacceptable for large data sets.
- Choice of pivot: If pick the leftmost/rightmost element of the partition as the pivot, the worst-case happens on
  already sorted array.
Algorithm:
- Pick an element, called a pivot, from the list.
- Reorder the list so that all elements with values less than the pivot come before the pivot, while all elements with
  values greater than the pivot come after it. After this partitioning, the pivot is at its final position.
- Recursively apply the above steps to the sub-list of elements with greater/smaller values respectively.
Simple version:
- Requires O(n) extra storage space, which is as bad as merge sort.
"""
import random


def partition(items, left, right):
    pivot = items[right]

    while left < right:
        while items[left] < pivot:
            left += 1
        while pivot < items[right]:
            right -= 1

        if items[left] == items[right]:
            left += 1
        elif left < right:
            items[left], items[right] = items[right], items[left]

    return right  # where the pivot is


def quick_sort(items, left, right):
    if left < right:
        part = partition(items, left, right)
        quick_sort(items, left, part-1)
        quick_sort(items, part+1, right)


# Test
random_items = [random.randint(-50, 100) for c in range(32)]
print(f"Before: {random_items}")

quick_sort(random_items, 0, len(random_items)-1)

print(f"After: {random_items}")
for i in range(len(random_items)-1):
    assert random_items[i] <= random_items[i+1]
