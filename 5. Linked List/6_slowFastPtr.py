"""
Here we are going to do 3 things - 
Cycle, length of cycle, start of cycle
Cycle - fast and slow to head, if they meet, cycle
length of cycle - when they meet, set a counter
start of cycle - when they meet -
                    1. Check if fast and fast.next is not none
                    2. Init fast to head, and inc fast by one, slow by one until they meet, 
                        where they meet is the starting point...
"""

def isCycle(head : ListNode) -> bool:

    if head is None:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
    
def cycleLength(head):
    
    # Match slow and fast pointer, then only increase head once...
    if head is None:
            return False

    slow = head
    fast = head

    while fast and fast.next:
        
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    fast = fast.next
    counter = 0
    while slow != fast:
        counter += 1
        fast = fast.next

    return counter


def startOfCycle(head):

    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if fast is None or fast.next is None:
        return None

    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    if slow == fast:
        return slow

    return None