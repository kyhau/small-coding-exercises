"""
https://leetcode.com/problems/available-captures-for-rook/
"""


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # Find R
        for row in board:
            if "R" in row:
                col = row.index("R")
                break

        # Discard "." in row
        r_str = "".join([r for r in row if r != "."])

        # Discard "." in board[r][col]
        c_str = "".join([r[col] for r in board if r[col] != "."])

        cnt = 0
        for s1 in ["pR", "Rp"]:
            for s2 in [r_str, c_str]:
                if s2.find(s1) > -1:
                    cnt += 1
        return cnt


"""
Sample Input:
[
[".",".",".",".",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".","R",".",".",".","p"],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".","p",".",".",".","."],
[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."]
]
Sample Output:
3
"""
