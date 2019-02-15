"""
https://leetcode.com/problems/di-string-match
"""


class Solution:
	def diStringMatch(self, S: 'str') -> 'List[int]':
		nums = [x for x in range(len(S) + 1)]

		ret = []
		for s in S:
			ret.append(nums.pop(0) if s == 'I' else nums.pop())
		ret.append(nums.pop())
		return ret

