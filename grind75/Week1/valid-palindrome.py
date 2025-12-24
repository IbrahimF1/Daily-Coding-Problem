# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        cleanedString = ""
        for char in s:
            if char.isalnum():
                cleanedString += char

        return cleanedString == cleanedString[::-1]
