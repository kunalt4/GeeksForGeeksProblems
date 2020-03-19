# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head:
            return
        
        first = head
        second = head.next
        oh = head
        
        if not second:
            return head
        
        head = second
        
        while first and first.next:

            first.next = second.next
            second.next = first
            first = first.next
            
            if first:
                second = first.next
                
            if oh.next and second:
                    oh.next = oh.next.next
                    oh = first
        return head
