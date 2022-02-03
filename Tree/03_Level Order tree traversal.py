class Node:
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return
    #create empty queue for level order trvaersal
    queue = []

    #enqueue root and initialise height
    queue.append(root)

    while (len(queue) > 0):

        #print front of queue and remove from queue
        print(queue[0].data)
        node = queue.pop(0)

        #enqueue left child
        if node.left:
            queue.append(node.left)

        #enqueue right child
        if node.right:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)



# 1
# 2
# 3
# 4
# 5