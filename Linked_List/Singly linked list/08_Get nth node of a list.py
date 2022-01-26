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

    def getNth(self, index):
        temp = self.head
        count=0
        while temp:
            if count == index:
                return temp.data
            count +=1
            temp = temp.next
        assert(false)
        return 0     

list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(8)
list.push(12)

print("Original list: ")
list.print_list()

print('\nNode at index 2 is:', list.getNth(2))


# Original list: 
# 12 8 4 3 2 1 
# Node at index 2 is: 4