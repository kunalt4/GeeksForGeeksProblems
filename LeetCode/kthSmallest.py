# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        stack = []
        while(k):
            
            if(node):
                stack.append(node)
                node = node.left
            else:
                finVal = stack.pop()
                k-=1
                node = finVal.right
        return finVal.val                
            
        