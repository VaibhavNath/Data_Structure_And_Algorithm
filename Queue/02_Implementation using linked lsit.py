class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self. front = self.rear = None
    
    def isempty(self):
        return self.front == None
    
    def Enqueue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
            return 

        self.rear.next = temp
        self.rear = temp

    def Dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None
        

if __name__ == "__main__":
    q=Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.Enqueue(40)
    print("Queue front is: "+ str(q.front.data))
    print("Queue rear is: "+ str(q.rear.data))



# Queue front is: 10
# Queue rear is: 40