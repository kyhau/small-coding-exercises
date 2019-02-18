"""
https://leetcode.com/problems/max-increase-to-keep-city-skyline/
"""


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        # i.e. find min of the max of the row and col
        rows = len(grid)
        cols = len(grid[0])

        rows_max = [max(grid[r]) for r in range(rows)]
        cols_max = [max([grid[r][c] for r in range(rows)]) for c in range(cols)]

        cnt = 0
        for r in range(rows):
            for c in range(cols):
                cnt += min(rows_max[r], cols_max[c]) - grid[r][c]
        return cnt


ret = Solution().maxIncreaseKeepingSkyline([
    [3, 0, 8, 4],
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
])
assert ret == 35
