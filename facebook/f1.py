"""
https://www.careercup.com/question?id=5732335291465728
"""

################################################################################
# Given an integer 'n', create an array such that each value is repeated twice.


def func1(n):
    ret = []
    for x in range(1, n+1):
        ret.extend([x]*2)
    print(ret)
    return ret


assert func1(3) == [1, 1, 2, 2, 3, 3]
assert func1(4) == [1, 1, 2, 2, 3, 3, 4, 4]


################################################################################
# Find a permutation such that each number is spaced in such a way, they are at
# a "their value" distance from the second occurrence of the same number.


def back_track(buf, n, ret):
    N = len(buf)
    if n == 0:
        print(buf)
        ret.append(buf)
        return
    for i in range(N - n - 1):
        j = i + n + 1
        print(buf, N, n, i, j) # uncomment to debug
        if buf[i] != 0 or buf[j] != 0:
            continue
        buf_next = list(buf) # deep copy
        buf_next[i] = buf_next[j] = n
        back_track(buf_next, n-1, ret)


def func2(n):
    buf = [0] * n * 2  # get the buf
    ret = []
    back_track(buf, n, ret)
    for i in ret: print(i)
    return ret

func2(4)
