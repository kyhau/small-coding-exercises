"""
https://leetcode.com/contest/weekly-contest-123/problems/broken-calculator/
"""


class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        if X >= Y:
            return X-Y

        if Y&1 == 0:
            return 1 + brokenCalc(X, Y/2)
        else:
            return 1 + brokenCalc(X, Y+1)


# {2 -> 4 -> 3}
assert Solution().brokenCalc(2, 3) == 2

# {5 -> 4 -> 8}
assert Solution().brokenCalc(5, 8) == 2

# {3 -> 6 -> 5 -> 10}
assert Solution().brokenCalc(3, 10) == 3

# Use decrement operations 1023 times
assert Solution().brokenCalc(1023, 1) == 1023
