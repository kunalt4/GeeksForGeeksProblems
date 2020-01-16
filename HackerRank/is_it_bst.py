""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    maxV = float('inf')
    minV = float('-inf')
    return checkBinary(root,minV,maxV)

def checkBinary(root, minV, maxV):
    
    if root is None:
        return True
    
    if root.data < minV or root.data > maxV:
        return False
    
    return (checkBinary(root.left,minV,root.data-1) and checkBinary(root.right,root.data+1,maxV))