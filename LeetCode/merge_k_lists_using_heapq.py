# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        head = cur = ListNode(0)
        q = []
        for idx, lst in enumerate(lists):
            if lst:
                heapq.heappush(q,(lst.val,idx,lst))
                
        while q:
            val,idx,node = heapq.heappop(q)
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(q,(node.val,idx,node))
                
        return head.next