# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeSortedPairofLists(list_a, list_b):
        if (list_a == None):
            return list_b
        elif (list_b == None):
            return list_a
        
        result = ListNode()
        head = result
        while list_a or list_b:
            if list_a == None:
                result.next = ListNode()
                result = result.next
                result.val = list_b.val
                list_b = list_b.next
            elif list_b == None:
                result.next = ListNode()
                result = result.next
                result.val = list_a.val
                list_a = list_a.next
            else:
                if list_a.val < list_b.val:
                    result.next = ListNode()
                    result = result.next
                    result.val = list_a.val
                    list_a = list_a.next
                else:
                    result.next = ListNode()
                    result = result.next
                    result.val = list_b.val
                    list_b = list_b.next
        return head.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        last_list_index = len(lists) - 1

        while (last_list_index > 0):
            i = 0
            j = last_list_index
            while (i < j):
                lists[i] = mergeSortedPairofLists(lists[i], lists[j])
                i += 1
                j -= 1
                if (i >= j):
                    last_list_index = j
 
        return lists[0]
