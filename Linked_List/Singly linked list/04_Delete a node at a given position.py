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

    def deleteNode(self, position):
        
        #check whether list is empty or not
        if self.head is None:
            return

        #if position is head of node
        if position == 0:
            self.head = self.head.next
            return self.head

        index = 0
        prev = self.head
        current = self.head
        temp = self.head

        while current:
            if (index == position) :
                temp = current.next
                break

            prev = current
            current = current.next
            index +=1
        prev.next = temp
        return prev     
        

list = Linked_list()

list.push(1)
list.push(2)
list.push(3)
list.push(4)

print("original list: ")
list.print_list()

list.deleteNode(1)
print('\nNew list: ')
list.print_list()


# original list: 
# 4 3 2 1 
# New list: 
# 4 2 1 