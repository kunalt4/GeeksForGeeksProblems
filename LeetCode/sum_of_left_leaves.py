# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        sumVal = 0
        
        queue = []
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            
            if node.left:
                if not node.left.left and not node.left.right:
                    sumVal += node.left.val
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return sumVal
        
