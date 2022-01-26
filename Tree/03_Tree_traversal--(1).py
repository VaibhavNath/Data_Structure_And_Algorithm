class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def inorder(temp):
    if temp:
        inorder(temp.left)
        print(temp.value, end=" ")
        inorder(temp.right)

def preorder(temp):
    if temp:
        print(temp.value, end=" ")
        preorder(temp.left)
        preorder(temp.right)

def postorder(temp):
    if temp:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.value, end=" ")
        

if __name__== '__main__' :
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)

    print(inorder(root))
    print(preorder(root))
    print(postorder(root))




        