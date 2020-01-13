# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        curSum = 0
        totSum = 0
        return self.sumTot(root, curSum, totSum)
    
    def sumTot(self,root, curSum, totSum):
        if(not root):
            return 0
        else:
            curSum = curSum*10 + root.val
            if(not root.right and not root.left):
                totSum = totSum + curSum
                return totSum
            return self.sumTot(root.left, curSum, totSum) + self.sumTot(root.right, curSum, totSum)
        
        