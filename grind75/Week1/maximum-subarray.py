# https://leetcode.com/problems/maximum-subarray
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            curSum = max(nums[i]+curSum, nums[i])
            result = max(result, curSum)

        return result
        
        
# @lc code=end