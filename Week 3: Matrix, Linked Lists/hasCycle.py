# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        slow_pointer = head
        fast_pointer = head

        while fast_pointer:
            if fast_pointer.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            else: #reached the end
                return False
            if fast_pointer == slow_pointer: #cycle
                return True
        
