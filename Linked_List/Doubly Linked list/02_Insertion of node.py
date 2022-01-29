class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doublycircularlinkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            
    #At the front of list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None

        #change prev of head node to newnode
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    #After a given node
    def InsertAfter(self, prev_node, new_data):

        #check is the given prev node is not null
        if prev_node is None:
            print("This node doesn't exists in linked list")
            return 

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        #change prev of newnode's next node
        if new_node.next:
            new_node.next.prev = new_node

    # At the end
    def append(self, new_data):
        new_node = Node(new_data)
        last = self.head
        new_node.next = None

        #if the list is empty make newnode as head node
        if self.head == None:
            new_node.prev = None
            self.head = new_node
            return

        #traverse till last node
        while last.next:
            last = last.next

        #change next of last node
        last.next = new_node

        #make last node as prev of newnode
        new_node.prev = last

  
list = Doublycircularlinkedlist()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)

print("original list:")
list.printlist()

list.InsertAfter(list.head.next.next,8)
print("\nlist after insertion of 8 is:")
list.printlist()

list.append(10)
print("\nlist after insertion of 10 is:")
list.printlist()


# original list:
# 5 4 3 2 1 
# list after insertion of 8 is:
# 5 4 3 8 2 1 
# list after insertion of 10 is:
# 5 4 3 8 2 1 10 