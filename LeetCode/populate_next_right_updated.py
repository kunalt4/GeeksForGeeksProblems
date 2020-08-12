"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        node = root
        
        while node and node.left:
            nextLevel = node.left
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left #else right is already None
                node = node.next
            node = nextLevel
        return root
