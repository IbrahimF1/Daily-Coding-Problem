# https://leetcode.com/problems/fizz-buzz/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def helper(i):
            # Base case: stop recursion
            if i == 0:
                return []

            # Recursive call: get results for 1..(i-1)
            result = helper(i - 1)

            # Determine FizzBuzz value for current i
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))

            return result
        
        return helper(n)
