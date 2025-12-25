# https://leetcode.com/problems/binary-search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        center = (right+left)//2

        while left <= right:
            center = (right+left)//2

            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center+1
            elif nums[center] > target:
                right = center-1

        return -1
