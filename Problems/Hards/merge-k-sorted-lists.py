# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        i = 0
        j = 0
        k = 0
        l_list = ListNode

        while k < len(lists):
            if lists[i] <= lists[j]:

            






