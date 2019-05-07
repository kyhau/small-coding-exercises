"""
https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        More expensive approach:
        import itertools
        ret = set([tuple(sorted(x)) for x in itertools.combinations(nums, 3) if sum(x) == 0])
        return [list(x) for x in ret]
        """
        res = []
        nums.sort()
        last_added = None

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # n1 + n2 + n3 = 0
            # n2 + n3 = -n1
            target = -nums[i]
            lo = i + 1
            hi = len(nums) - 1

            while lo < hi:
                if nums[lo] + nums[hi] > target:
                    hi -= 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    to_add = [nums[i], nums[lo], nums[hi]]
                    if last_added != to_add:
                        res.append(to_add)
                        last_added = to_add
                    hi -= 1
        return res
