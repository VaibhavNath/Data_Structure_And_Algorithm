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

    def is_palindrome(self):
        temp = self.head
        stack=[]
        ispalin = True
        while temp:
            stack.append(temp.data)
            temp = temp.next

        while(self.head):
            i = stack.pop()
            if self.head.data == i:
                ispalin = True
            else:
                ispalin = False
            self.head = self.head.next
        return ispalin
    


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

print('\n',list.is_palindrome())