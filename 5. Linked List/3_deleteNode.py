# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        curr = node.next

        while curr:
            
            if curr.next is None:
                prev.next = None
            prev.val = curr.val
            prev = curr
            curr = curr.next
                
            
                
            
                