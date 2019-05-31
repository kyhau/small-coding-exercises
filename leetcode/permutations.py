"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/

Given a collection of distinct integers, return all possible permutations.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l == 1:
            return [nums]

        a = nums[0]
        small = self.permute(nums[1:])
        ret = []
        for s in small:
            for i in range(len(s) + 1):
                ret.append(s[:i] + [a] + s[i:])
        return ret


# Test
input = [1,2,3]
expected = [[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]
assert Solution().permute(input) == expected