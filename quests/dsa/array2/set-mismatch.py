# https://leetcode.com/problems/set-mismatch

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        setNums = set(nums)

        missing = 0
        duplicate = 0
        existing = set()
        for i in range(1, len(nums)+1):
            if i not in setNums:
                missing = i


        for i in nums:
            if i in existing:
                duplicate = i
            else:
                existing.add(i)

        if duplicate == 0:
            duplicate = len(nums)+1

        return [duplicate, missing]