"""
https://leetcode.com/problems/two-sum-sum-of-bst/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = 0
        d = {}
        while pos < len(nums):
            value = nums[pos]
            diff = target - value
            if diff in d:
                return [d[diff], pos]
            d[value] = pos
            pos += 1
