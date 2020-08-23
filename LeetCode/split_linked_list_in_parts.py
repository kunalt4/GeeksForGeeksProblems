# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        curr = root
        length = 0
        
        while curr:
            curr = curr.next
            length+=1
            
        min_length = length // k
        rem = length % k
        curr = root
        prev = None
        
        res = []
        for i in range(k):
            part = []
            
            if curr:
                res.append(curr)
                for j in range(min_length):
                    prev = curr
                    curr = curr.next

                if i < rem:
                    prev = curr
                    curr = curr.next
                prev.next = None
            
            else:
                res.append(None)
                
        return res
