# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left
            
            parent = root.right
            tmp = parent.left
            while tmp and tmp.left:
                parent = parent.left
                tmp = tmp.left
            if tmp:
                parent.left = tmp.right
                tmp.left = root.left
                tmp.right = root.right
                root.left, root.right = None, None
                return tmp
            else:
                parent.left = root.left
                root.left, root.right = None, None
                return parent
        return root
            
            
