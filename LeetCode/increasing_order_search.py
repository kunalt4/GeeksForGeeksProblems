# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Poor approach
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stackTree = []
        res = []
        cur = root
        stackTree.append(cur)
        while stackTree:
            while cur:
                cur = cur.left
                stackTree.append(cur)
            cur = stackTree.pop()
            if cur:
                res.append(TreeNode(cur.val))
                cur = cur.right
                stackTree.append(cur)
        i = 0
        while i<len(res)-1:
            res[i].right = res[i+1]
            i+=1
        return res[0]
        
