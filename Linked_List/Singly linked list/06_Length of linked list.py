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

    def getCount(self):
        temp=self.head
        count=0
        while (temp):
            count +=1
            temp = temp.next
        print ("\nNumber of nodes in linked list:", count)
    


list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(8)
list.push(12)

print("Original list: ")
list.print_list()

list.getCount()

# original list: 
# 12 8 4 3 2 1 
# Number of nodes in linked list: 6