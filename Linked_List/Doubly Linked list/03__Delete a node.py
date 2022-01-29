import gc

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
            
    #At the front of list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None

        #change prev of head node to newnode
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def delete(self, dele):
        if self.head is None or dele is None:
            return
        if self.head == dele:
            self.head = dele.next
        if dele.next:
            dele.next.prev = dele.prev
        if dele.prev:
            dele.prev.next = dele.next
        gc.collect

   

  
list = Doublycircularlinkedlist()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)

print("original list:")
list.printlist()

list.delete(list.head)
print("\nlist after deletion is:")
list.printlist()

list.delete(list.head.next)
print("\nlist after deletion is:")
list.printlist()
