# https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        """
        storing the node after the current node (2nd node)
        
        inner swapPairs is fed the node after the next node (3rd node):
            if 3rd node exists:
                returns the node after the 3rd node (4th node)
            if 3rd node doesn't exist:
                return none
                
        currend node points to anything returned anything that is returned by inner swapPairs (4th node)
        1 -> 4
        
        point the node after the current node (2nd node) to the current node (1st node)
        2 -> 1
        
        """
        if head == None or head.next == None:
            return head
            
        head2 = head.next
        
        head.next = self.swapPairs(head2.next)
        
        head2.next = head
        
        return head2