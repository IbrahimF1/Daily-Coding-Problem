# https://leetcode.com/problems/search-insert-position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        center = (right+left)//2
        while left < right:
            if center ==
