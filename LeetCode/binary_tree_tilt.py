# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        self.tilt = 0
        self.storeTilt(root)
        return self.tilt
        
    def storeTilt(self, root):
        if not root:
            return 0
        
        left_tilt = self.storeTilt(root.left)
        right_tilt = self.storeTilt(root.right)
                
        self.tilt += abs(left_tilt - right_tilt)
        
        return root.val + left_tilt + right_tilt
