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
        head_dict = {}

        while headA.next != None or headB.next != None:
            if headA.next != None:
                if headA in head_dict:
                    return headA
                head_dict[headA] = 1
                headA = headA.next

            if headB.next != None:
                if headB in head_dict:
                    return headB
                head_dict[headB] = 1

                headB = headB.next
        
        return headB if headA == headB else None
        