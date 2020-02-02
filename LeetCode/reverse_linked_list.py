# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        next_p = None
        while node:
            next_p = node.next
            node.next = prev
            prev = node
            node = next_p
        return prev
            
