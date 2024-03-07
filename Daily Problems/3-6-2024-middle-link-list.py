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
        curr_node = head
        node_list = []

        while curr_node != None:
            node_list.append(curr_node)

            curr_node = curr_node.next

        list_len = len(node_list) - 1
        mid_node = (list_len // 2) + (list_len % 2)

        return(node_list[mid_node])