# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stackTree = []
        res = []
        curr = root
        stackTree.append(curr)
        while(stackTree):
            while(curr):
                curr = curr.left
                stackTree.append(curr)
            curr = stackTree.pop()
            if curr:
                res.append(curr.val)
                curr = curr.right
                stackTree.append(curr)
        return res