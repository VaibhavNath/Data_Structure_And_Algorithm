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
            print(temp.data ,  end=" ")
            temp = temp.next
        

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def Count(self ,key):
        current = self.head
        count = 0
        while current:
            if current.data == key:
                count +=1
            current = current.next
        print(f'\nNumber of times the given element {key} occurs in linked list is:' , count)
        
        
list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(54)
list.push(3)
list.push(12)

print("Original list: ")
list.print_list()

list.Count(3)


# Original list: 
# 12 3 54 4 3 2 1 
# Number of times the given element 3 occurs in linked list is: 2