# https://leetcode.com/problems/last-stone-weight
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heapStones = [-x for x in stones]
        heapq.heapify(heapStones)

        while len(heapStones) > 1:
            x = -heapq.heappop(heapStones)
            y = -heapq.heappop(heapStones)

            if x != y:
                heapq.heappush(heapStones, y - x)

        if heapStones:
            return -heapStones[0]
        
        return 0
        
        
# @lc code=end

