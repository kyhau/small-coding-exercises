"""
https://leetcode.com/problems/flipping-an-image/
"""


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for r in A:
            r.reverse()
            for c in range(len(r)):
                r[c] ^= 1
        return A


assert Solution().flipAndInvertImage(
    [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

assert Solution().flipAndInvertImage(
    [[1,1,0],[1,0,1],[0,0,0]]
) == [[1,0,0],[0,1,0],[1,1,1]]

"""
1 1 0
1 0 1
0 0 0

0 1 1
1 0 1
0 0 0

1 0 0
0 1 0
1 1 1
"""
