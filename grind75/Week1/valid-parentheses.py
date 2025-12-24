# https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tracker = []

        for i in s:
            if i == '(':
                tracker.append("round")
            elif i == '[':
                tracker.append("square")
            elif i == '{':
                tracker.append("curly")
            elif i == ')':
                if len(tracker) < 1 or tracker.pop() != "round":
                    return False
            elif i == ']':
                if len(tracker) < 1 or tracker.pop() != "square":
                    return False
            elif i == '}':
                if len(tracker) < 1 or tracker.pop() != "curly":
                    return False

        if len(tracker) > 0:
            return False

        return True
