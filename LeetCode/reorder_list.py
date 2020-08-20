# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            midStartpoint = self.getMid(head)
            rev, end = self.reverseList(midStartpoint)
            midStartpoint.next = rev
            end.next = None

            start = head
            while start.next != midStartpoint:
                start = start.next
            start.next = None

            start = head
            temp1 = start
            temp2 = rev

            while start and rev:
                temp1 = start.next
                temp2 = rev.next
                start.next = rev
                rev.next = temp1
                start = temp1
                rev = temp2
                
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        next_p = None
        while node:
            next_p = node.next
            node.next = prev
            prev = node
            node = next_p
        return prev, head
    
    
    def getMid(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            return slow.next
        return slow
