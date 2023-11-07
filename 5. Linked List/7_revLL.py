# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        """
        I used the code from reorder linked list... Its the same with last modification,
        traverse till mid
        reverse the list from mid.next to end
        Compare the first list with the second.. then get the ans...
        """
        
        if head is None:
            return True
        
        # get mid point of the lists
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # disconnect the 2 lists
        right = slow.next
        slow.next = None
        left = head
        
        # reverse right half
        prev = None
        curr = right
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        right = prev
        left = head
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True