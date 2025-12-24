# https://leetcode.com/problems/valid-anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freqTracker1 = dict()
        freqTracker2 = dict()

        for letter in s:
            if letter in freqTracker1:
                freqTracker1[letter] += 1
            else:
                freqTracker1[letter] = 1

        for letter in t:
            if letter in freqTracker2:
                freqTracker2[letter] += 1
            else:
                freqTracker2[letter] = 1

        return freqTracker1 == freqTracker2
