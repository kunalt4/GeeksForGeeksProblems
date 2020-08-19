# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return []

        res = []

        self.treePath(root, str(root.val), res, 0)

        return sum(res)

    def treePath(self, node, cur_path, res, num):
        
        num = num * 2
        num = num + int(cur_path)

        if not node.left and not node.right:
            res.append(num)
            return

        if node.left:
            self.treePath(node.left, str(node.left.val), res, num)

        if node.right:
            self.treePath(node.right, str(node.right.val), res, num)
            
