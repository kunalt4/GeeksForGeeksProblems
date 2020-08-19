# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        if not root:
            return []
        
        res = []
        
        self.treePath(root, str(root.val), res)
        
        return res
        
    def treePath(self, node, cur_path, res):
        
        if not node.left and not node.right:
            res.append(cur_path)
            return
        
        if node.left:
            self.treePath(node.left, cur_path + "->" + str(node.left.val), res)
            
        if node.right:
            self.treePath(node.right, cur_path + "->" + str(node.right.val), res)
