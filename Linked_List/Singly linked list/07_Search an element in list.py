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

    def search(self, x):
        current = self.head
        while current:
            if current.data == x:
                return True
            current = current.next
        return False
    


list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(8)
list.push(12)

print("Original list: ")
list.print_list()

print('\n',list.search(4))
print('\n',list.search(10))



