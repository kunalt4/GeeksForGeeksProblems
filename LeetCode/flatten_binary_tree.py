# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    prev = None 
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        self.prev = root
        self.flatten(root.left)
        
        temp = root.right
        root.right, root.left = root.left, None
        self.prev.right = temp
        
        self.flatten(temp)
        