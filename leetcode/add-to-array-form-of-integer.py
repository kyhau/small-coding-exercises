"""
https://leetcode.com/contest/weekly-contest-123/problems/add-to-array-form-of-integer/
"""


class Solution:
	def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
		return [int(x) for x in list(str(int("".join([str(x) for x in A])) + K))]
