class Node:    
    def __init__(self, data):
        self.value=data
        self.left=None
        self.right=None

#           1
#          /  \
#        2      3
#       / \    / \
#      4   5  6   7

def inorder(temp):
    if temp:
        inorder(temp.left)
        print(temp.value,end=" "),
        inorder(temp.right)

def preorder(temp):
    if temp:
        print(temp.value,end=" "),
        preorder(temp.left)
        preorder(temp.right)

def postorder(temp):
    if temp:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.value,end=" "),
        

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

print ("Preorder traversal of binary tree is")
preorder(root)
 
print ("\nInorder traversal of binary tree is")
inorder(root)
 
print ("\nPostorder traversal of binary tree is")
postorder(root)



# Preorder traversal of binary tree is
# 1 2 4 5 3 
# Inorder traversal of binary tree is
# 4 2 5 1 3 
# Postorder traversal of binary tree is
# 4 5 2 3 1 
        