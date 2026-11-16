# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        linkedSet = set()
        pointer = head 
        while pointer : 
            if pointer in linkedSet:
                return True
            else:
                linkedSet.add(pointer)
            pointer=pointer.next
        return False 
        '''
        slow = head 
        fast = head
        while fast and fast.next :
            if slow == fast : 
                return True
            slow = slow.next
            fast = fast.next.next
        return False
        '''
        