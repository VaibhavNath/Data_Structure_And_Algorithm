class Node:
    #function to initialise node object
    def __init__(self, data):
        self.data = data   #assign data
        self.next = None   #initialise next as null

#linked list class contains a node object
class Linked_list:
    #function to initialise head
    def __init__(self):
        self.head = None
   
    # Traverse a linked list.
    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data , end=" ")
            temp = temp.next

#code execution starts here
if __name__ == '__main__' :

    #start with empty list
    list = Linked_list()

    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    #link nodes to each other
    list.head.next=second
    second.next=third

    list.print_list()     # 1 2 3