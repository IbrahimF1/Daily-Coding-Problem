# https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i = len(digits) - 1
        while digits[i] == 9 and i > -1:
            digits[i] = 0
            i -= 1

        if i == -1:
            digits = [1] + digits
            return digits
        else:
            digits[i] += 1
            return digits
