# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        
        self.addRow(root, v, d, 2)
        return root
    
    def addRow(self, root, v, d, curr_depth):
        
        if not root:
            return
        
        if d == curr_depth:
            
            if root.left:
                left_node = TreeNode(v)
                left_node.left = root.left
                root.left = left_node
            else:
                left_node = TreeNode(v)
                root.left = left_node
            if root.right:
                right_node = TreeNode(v)
                right_node.right = root.right
                root.right = right_node
            else:
                right_node = TreeNode(v)
                root.right = right_node
                
        else:
            self.addRow(root.left, v, d, curr_depth+1)
            self.addRow(root.right, v, d, curr_depth+1)
