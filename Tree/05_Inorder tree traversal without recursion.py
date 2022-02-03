class Node:
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None

def inorder(root):
    #set current to root of tree
    current = root

    #initialise stack
    stack =[]
    while True:

        #reach leftmost node of current node
        if current:
            stack.append(current)
            current = current.left

        #backtrack from empty subtree and visit node at top of stack , if stack is empty then exit
        elif(stack):
            current = stack.pop()
            print(current.data, end =" ")

            #we have visited the node and left subtree now visit right subtree
            current = current.right

        else:
            break

    print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)   # 4 2 5 1 3