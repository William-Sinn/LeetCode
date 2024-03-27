# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast_point = head
        slow_point = head

        while fast_point is not None and fast_point.next is not None:
            fast_point = fast_point.next.next
            slow_point = slow_point.next

        return(slow_point)