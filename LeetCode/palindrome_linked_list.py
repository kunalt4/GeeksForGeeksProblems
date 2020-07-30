# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        new = None
        while slow:
            n = slow.next
            slow.next = new
            new = slow
            slow = n
        
        while new:
            if head.val != new.val:
                return False
            head = head.next
            new = new.next
        return True
