''' This is a function problem.You only need to complete the function given below '''
'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
#Your task is to complete this function
#function should return head to the DLL
def bToDLL(root):
    # do Code here
    prev = None
    head = None
    head, prev = btoDL(root, head, prev)
    return head
    
def btoDL(root,head, prev):
    if(root.left):
        head, prev = btoDL(root.left, head, prev)
    if(prev is None):
        head = root
    else:
        root.left = prev
        prev.right = root
    prev = root
    if(root.right):
        head, prev = btoDL(root.right, head, prev)
    return head, prev