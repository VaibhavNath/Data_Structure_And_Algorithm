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
        

        #change prev of head node to newnode
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def Reverse(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        if temp:
            self.head = temp.prev 

        
  
list = Doublycircularlinkedlist()
list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)

print("original list:")
list.printlist()

list.Reverse()
print("\nlist after reverse:")
list.printlist()



# original list:
# 5 4 3 2 1 
# list after reverse:
# 1 2 3 4 5 