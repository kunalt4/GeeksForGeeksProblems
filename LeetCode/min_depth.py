# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        que = []
        que.append((root,1))
        
        while que:
            
            node, height = que.pop(0)
            
            if not node.left and not node.right:
                return height
            
            if node.left:
                que.append((node.left, height+1))
                
            if node.right:
                que.append((node.right, height+1))
        
       
