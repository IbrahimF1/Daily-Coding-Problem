# https://leetcode.com/problems/power-of-two

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        """
        if n less than 0:
            return false
            
        if n less than 1:
            x decreases
            
            if currNum is < n:
                return False
            
        if n greater than 1:
            x increases
            
            if currNum is < n:
                return True
        """
        
        def helper(n, currNum):
            if n <= 0:
                return False
                
            if currNum == n:
                return True
            
            if n < 1:
                if currNum < n:
                    return False
    
                return helper(n, currNum / 2)
                
            if n > 1:
                if currNum > n:
                    return False
    
                return helper(n, currNum * 2)
                
                
        return helper(n, 1)
                