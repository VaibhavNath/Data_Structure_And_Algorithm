class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp=self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def detect_loop(self):
        slow = self.head
        fast = self.head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                print('\nLoop Found')
        print("\nLoop not Found")


list=Linkedlist()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(1)

print("Original list is: ")
list.print_list()

list.detect_loop()


# Original list is: 
# 1 4 3 2 1 
# Loop not found