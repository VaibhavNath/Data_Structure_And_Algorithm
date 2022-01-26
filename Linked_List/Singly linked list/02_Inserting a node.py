class Node:
    #function to initialise node object
    def __init__(self, data):
        self.data = data   #assign data
        self.next = None   #initialise next as null

#linked list class contains a node object
class Linked_list:
    #function to initialise head
    def __init__(self):
        self.head = None
   
    # Traverse a linked list.
    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data , end=" ")
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def InsertAfter(self, prev_node, new_data):
        #check if prev_node exists
        if prev_node is None:
            print("Given prev node is not in list")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        #if head is none make newnode as head
        if self.head is None:
            self.head = new_node
            return
        
        #else traverse the list till last node
        last = self.head
        while (last.next):
            last = last.next

        last.next=new_node  
      

list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)

print("original list: ")
list.print_list()

list.InsertAfter(list.head.next,7)
print("\nlist after insertion of new node is: ")
list.print_list()

list.append(10)
print('\nNew list: ')
list.print_list()



# original list: 
# 4 3 2 1 
# list after insertion of new node is: 
# 4 3 7 2 1 
# New list: 
# 4 3 7 2 1 10 