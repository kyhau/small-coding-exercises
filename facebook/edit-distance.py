"""
Write a function to return if two words are exactly "one edit" away, where an edit is:
- Inserting one character anywhere in the word (including at the beginning and end)
- Removing one character
- Replacing exactly one character
"""


def is_one_edit(w1, w2):
    """
    Time complexity: O(n)
    Auxiliary Space: O(1)
    """
    len1 = len(w1)
    len2 = len(w2)

    if abs(len1-len2) > 1:
        return False

    diff, pos1, pos2 = 0, 0, 0
    while pos1 < len1 and pos2 < len2:
        if w1[pos1] == w2[pos2]:
            pos1+=1
            pos2+=1
        else:
            diff += 1
            if diff > 1:
                return False
            if len1 == len2:
                pos1 += 1
                pos2 += 1
            elif len1 > len2:
                pos1 += 1
            else:
                pos2 += 1

    # if last char is extra
    if pos1 < len1 or pos2 < len2:
        diff += 1

    # exactly one
    return diff == 1


# Inserting one character anywhere in the word (including at the beginning and end)
# Removing one character
assert is_one_edit("abcdefg", "bcdefg")
assert is_one_edit("abcdefg", "abcdef")
assert is_one_edit("abcdefg", "abdefg")

# Replacing exactly one character
assert is_one_edit("abcdefg", "zbcdefg")
assert is_one_edit("abcdefg", "abcdefz")
assert is_one_edit("abcdefg", "abczefg")

assert not is_one_edit("abcdefg", "abcdefg")    # no edit
assert not is_one_edit("abcdefg", "abcdeFG")    # 2 edit
assert not is_one_edit("abcdefg", "abcdefghi")  # 2 edit

assert is_one_edit("cat", "cats")
assert is_one_edit("cat", "cut")
assert is_one_edit("cat", "cast")
assert is_one_edit("cat", "at")
assert not is_one_edit("cat", "act")
assert not is_one_edit("cat", "dog") 
