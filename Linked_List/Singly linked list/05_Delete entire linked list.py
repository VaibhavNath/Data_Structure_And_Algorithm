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

    def delete_list(self):
        #initialise current node
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev 

            #OR

        # in python garbage collection happens thus this line also elete the list
        self.head = None


list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)

print("original list: ")
list.print_list()

list.delete_list()