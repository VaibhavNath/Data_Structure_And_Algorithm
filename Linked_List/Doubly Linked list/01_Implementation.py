class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doublycircularlinkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__' :   

    list = Doublycircularlinkedlist()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)

    list.head.next = second
    second.next = third
    third.next = None

    list.head.prev = None
    second.prev = list.head.next
    third.prev = second.next

    list.printlist()


# 1 2 3 