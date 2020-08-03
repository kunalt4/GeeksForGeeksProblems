# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def leftRightBalance(root):
            
            if root is None:
                return 0
            
            left = leftRightBalance(root.left)
            
            if left == -1:
                return -1
            
            right = leftRightBalance(root.right)
            
            if right == -1 or abs(left-right) > 1:
                return -1
            
            return 1+max(left,right)
    
        return leftRightBalance(root) != -1
