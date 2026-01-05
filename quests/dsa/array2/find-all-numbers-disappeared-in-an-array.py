# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        setNums = set(nums)

        result = []
        for i in range(1,len(nums)+1):
            if i not in setNums:
                result.append(i)

        return result