"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

Given a `m x n` matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c, r = set(), set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    r.add(row)
                    c.add(col)

        for col in c:
            for row in range(len(matrix)):
                matrix[row][col] = 0

        for row in r:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0


print("Test 1")
test_1 = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
expected_1 = [
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Solution().setZeroes(test_1)
assert test_1 == expected_1

print("Test 2")
test_2 = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
expected_2 = [
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Solution().setZeroes(test_2)
assert test_2 == expected_2
