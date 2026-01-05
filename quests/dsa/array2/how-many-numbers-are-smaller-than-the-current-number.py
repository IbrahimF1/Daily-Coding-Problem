# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedNums = sorted(nums)
        
        smallerMap = {}
        for i in range(len(sortedNums)):
            if sortedNums[i] in smallerMap:
                continue
            smallerMap[sortedNums[i]] = i

        result = []
        for i in nums:
            result.append(smallerMap[i])

        return result