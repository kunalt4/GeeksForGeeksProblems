# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]
        
        sum -= root.val
        
        tmp = (self.pathSum(root.left, sum) + self.pathSum(root.right, sum))
        return [[root.val]+i for i in tmp]
