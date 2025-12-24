# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tracker = {}

        for i in range(len(nums)):
            if target - nums[i] in tracker:
                return [tracker[target - nums[i]], i]
            tracker[nums[i]] = i
