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

    def deleteNode(self, key):
        temp=self.head

        #if head itself hold key to be deleted
        if temp:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        #search for key to be deleted,keep track of prev_node
        while (temp):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next 

        #if key is not present in list
        if temp == None:
            return

        #unlink node from linked list
        prev.next = temp.next
        temp =None

list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)

print("original list: ")
list.print_list()

list.deleteNode(2)
print('\nNew list: ')
list.print_list()



# original list: 
# 4 3 2 1 
# New list: 
# 4 3 1 