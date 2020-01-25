# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        node = head
        count = 0
        G = set(G)
        while(node.next):
            if node.val in G and node.next.val not in G:
                count+=1
            node = node.next
        if node.val in G:
            return count + 1
        return count