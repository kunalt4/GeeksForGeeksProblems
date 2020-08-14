# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        res = []
        que = []
        que.append(root)
        
        while(len(que) > 0):
            lev = []
            for i in range(len(que)):
                node = que.pop(0)
                lev.append(node.val)
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(lev)
        
        return res[::-1]
