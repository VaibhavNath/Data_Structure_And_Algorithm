class Node:
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None

def inorder(temp):
    if temp:
        inorder(temp.left)
        print(temp.data,end=" "),
        inorder(temp.right)

def insert(temp, data):
    if not temp:
        root = Node(data)
        return

    q=[]
    q.append(temp)

    # do level orfer traversal untill we find an empty space
    while(len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = Node(data)
            break
        else:
            q.append(temp.left)

        if (not temp.left):
            temp.left = Node(data)
            break
        else:
            q.append(temp.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)         

    inorder(root)
    data = 12
    insert(root, data)
    print()
    inorder(root)  



# 4 2 5 1 3 
# 4 2 5 1 12 3 