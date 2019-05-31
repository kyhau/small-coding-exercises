

def binary_search(sorted_list, value):

    def func(sorted_list, start_pos, end_pos):
        if start_pos >= end_pos:
            return -1

        mid = (start_pos + end_pos) // 2
        if value == sorted_list[mid]:
            return mid
        if value < sorted_list[mid]:
            return func(sorted_list, start_pos, mid-1)
        return func(sorted_list, mid+1, end_pos)

    return func(sorted_list, 0, len(sorted_list)-1)


# Test
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert binary_search(items, 8) == 7

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert binary_search(items, 5) == 4

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert binary_search(items, 5) == 4

items = [1, 2, 3, 4, 5, 5, 7, 8, 9, 10]
assert binary_search(items, 5) == 4

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert binary_search(items, 11) == -1
