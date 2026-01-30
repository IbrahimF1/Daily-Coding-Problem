# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        index = 0
        for i in range(nums[0], nums[-1]+1):
            if i in nums_set:
                nums[index] = i
                index+=1

        return index
        
# @lc code=end

