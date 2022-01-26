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
            print(str(temp.data) , '->', end=" ")
            temp = temp.next
        print('NULL')

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def Middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print('Middle element is:' , slow.data)

    
    
list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(54)
list.push(8)
list.push(12)

print("Original list: ")
list.print_list()

list.Middle()