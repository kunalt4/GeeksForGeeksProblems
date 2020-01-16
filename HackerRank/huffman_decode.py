

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    temp = root
    for char in s:
        if char == '0':
            temp = temp.left
        else:
            temp = temp.right
        if not temp.left and not temp.right:
            print(temp.data, end="")
            temp = root

