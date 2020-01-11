# https://leetcode.com/problems/add-two-numbers/ 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = p3 = ListNode((l1.val+l2.val)%10)
        carry = ((l1.val+l2.val)//10)
        l1 = l1.next
        l2 = l2.next
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
                
            val = v1+v2+carry
            carry = val//10
            val = val%10
            p3.next = ListNode(val)
            p3 = p3.next
        return l3   