# https://leetcode.com/problems/max-consecutive-ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                result = max(counter, result)
                counter = 0

        result = max(counter, result)

        return result