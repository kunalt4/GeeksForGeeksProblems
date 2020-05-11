# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def isMirror(left, right):
            
            if not left and not right:
                return True
            
            elif left and right:
                if left.val == right.val:
                    check_one = isMirror(left.left, right.right)
                    check_two = isMirror(left.right,right.left)
                    return check_one and check_two
                else:
                    return False
                
            elif left or right:
                return False
        
        if root is None:
            return True
        else:
            return isMirror(root.left, root.right)
