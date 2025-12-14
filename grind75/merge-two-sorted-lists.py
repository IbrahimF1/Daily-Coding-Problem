# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        result = head

        while list1 != None and list2 != None:
            
            if list1.val >= list2.val:
                head.next = ListNode(list2.val)
                list2 = list2.next
                head = head.next
            elif list1.val <= list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next
                head = head.next

        if list1 != None:
            head.next = list1
        else:
            head.next = list2

        return result.next
