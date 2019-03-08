"""
https://leetcode.com/problems/rotting-oranges/
"""
import copy


class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        rows = len(grid)
        cols = len(grid[0])

        def found_value(grid, value):
            found = []
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == value:
                        found.append((r, c))
            return found

        found_1 = found_value(grid, 1)
        if not found_1:
            return 0

        t = 0
        while found_1:
            grid0 = copy.deepcopy(grid)
            changed = False
            for (r, c) in found_1:
                for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= x < rows and 0 <= y < cols:
                        if grid[x][y] == 2:
                            grid0[r][c] = 2
                            changed = True
            if changed is False:
                break
            t += 1
            grid = grid0
            found_1 = found_value(grid, 1)

        if found_1:
            return -1
        return t


assert Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert Solution().orangesRotting([[0,2]]) == 0
