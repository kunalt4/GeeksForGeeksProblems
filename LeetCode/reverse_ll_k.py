# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        node = head
        length = 0
        while node:
            length+=1
            node = node.next
        k = k%length
        if k == 0:
            return head
        node = head
        nextnode = node
        for i in range(length-k-1):
            node = node.next
            nextnode = node.next
        while nextnode and nextnode.next:
            nextnode = nextnode.next
        nextnode.next = head
        head = node.next
        node.next = None
        return head