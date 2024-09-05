# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next if pA is not None else headB
            pB = pB.next if pB is not None else headA
        
        return pA
        