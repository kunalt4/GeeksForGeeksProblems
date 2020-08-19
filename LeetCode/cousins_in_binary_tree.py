# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x_depth = -1
        self.y_depth = -2
        self.x_parent = None
        self.y_parent = None
        self.is_cousin(root, None, x, y, 0)
        return self.x_depth == self.y_depth and self.x_parent != self.y_parent
    
    def is_cousin(self, node, parent, x, y, height):
        
        if node is None:
            return
        
        if node.val in (x,y):
        
            if node.val == x:
                self.x_depth = height
                self.x_parent = parent
            
            if node.val == y:
                self.y_depth = height
                self.y_parent = parent
        else:
            
            self.is_cousin(node.left, node, x, y, height+1)
            self.is_cousin(node.right, node, x, y, height+1)
        
        
        
