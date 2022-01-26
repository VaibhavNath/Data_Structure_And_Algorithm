from sqlalchemy import false

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

    def movetofront(self):
        temp = self.head
        second_last = None

        #chcek for empty list or one node list
        if not temp or not temp.next:
            return 
        while temp and temp.next:
            second_last = temp
            temp = temp.next

        second_last.next = None
        temp.next = self.head
        self.head = temp

    
list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(3)
list.push(2)
list.push(1)

print("Original list: ")
list.print_list()

list.movetofront()
print('\nlist after moving element:')
list.print_list()

