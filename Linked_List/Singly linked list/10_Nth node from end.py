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

    def getNthfromEnd(self, n):
        temp = self.head
        length = 0
        while temp:
            temp = temp.next
            length +=1
        if n > length :
            print("\nLocation is greater than length of linked list")
            return

        temp=self.head
        for i in range (0, length-n ):
            temp = temp.next
       
        print(f'\n{n}th Node from end is:',temp.data)
        

list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(8)
list.push(12)

print("Original list: ")
list.print_list()

list.getNthfromEnd(4)


# Original list: 
# 12 8 4 3 2 1 
# 5th Node from end is: 8