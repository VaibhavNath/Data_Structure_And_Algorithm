class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None   

class Linked_list:
    def __init__(self):
        self.head = None
   
    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data , end=" ")
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def swapNodes(self, x, y):

        #if x and y are same then return
        if x == y:
            return

        #Search for X (keep track of prevX and currX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        #Search for Y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        #if either x or y is not present then return
        if currX == None or currY == None:
            return

        #if x is not head of the list:
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

        #if y is not head of the list:
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        #swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    
list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(8)
list.push(12)

print("Original list: ")
list.print_list()

list.swapNodes(12, 2)
print("\nNew list:")
list.print_list()

# original list: 
# 12 8 4 3 2 1 
# Number of nodes in linked list: 6