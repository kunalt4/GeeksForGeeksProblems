# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return
        
        directionFlag = True
        res = []
        q = []
        
        q.append(root)
        
        while(len(q)>0):
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                
                if node.left: 
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            if directionFlag:
                res.append(level)
            else:
                res.append(level[::-1])
            
            directionFlag = not directionFlag
            
        return res
