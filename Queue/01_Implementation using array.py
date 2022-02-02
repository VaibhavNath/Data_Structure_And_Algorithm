class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.rear = capacity -1
        self.data = []
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def isfull(self):
        return self.size == self.capacity
    
    def enqueue(self, e):
        if self.isfull():
            print("Queue is full")
            return
        self.data.append(e)
        self.size = self.size + 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = self.front + 1
        self.size = self.size -1
        return value
    
    def get_first(self):
        if self.isEmpty():
            print("Queue is empty")
        return self.data[self.front]

    def get_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        return self.data[self.rear]


q = Queue(10)
q.enqueue(10)
q.enqueue(20)
print("Queue:" ,q.data)
print("length:", len(q))
q.enqueue(30)
q.enqueue(40)
print("Queue: " ,q.data)
print("Dequeue:",q.dequeue())
print("Queue: " ,q.data)
print("Front is:",q.get_first())
print("Dequeue:",q.dequeue())
print("Queue: " ,q.data)
print("Rear is:", q.get_rear())


# Queue: [10, 20]
# length: 2
# Queue:  [10, 20, 30, 40]
# Dequeue: 10
# Queue:  [None, 20, 30, 40]      
# Front is: 20
# Dequeue: 20
# Queue:  [None, None, 30, 40]