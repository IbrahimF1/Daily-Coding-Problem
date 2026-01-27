# https://leetcode.com/problems/search-insert-position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        
        while left < right:
            center = (right+left)//2
            if nums[center] == target:
                return center

            if nums[center] > target:
                right = center # don't include - 1
            if nums[center] < target:
                left = center + 1

        return left
