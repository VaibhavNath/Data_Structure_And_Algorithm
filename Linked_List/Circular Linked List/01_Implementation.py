class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circularlinkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        temp = self.head

        if self.head:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = new_node

        else:
            new_node.next = new_node

        self.head = new_node

    def printlist(self):
        temp = self.head
        if self.head:
            while (True):
                print(temp.data, end=" " )
                temp = temp.next
                if (temp == self.head):
                    break

list=Circularlinkedlist()
list.push(1)                
list.push(2)                
list.push(3)                
list.push(4)                
list.push(5)

list.printlist()


# 5 4 3 2 1
            