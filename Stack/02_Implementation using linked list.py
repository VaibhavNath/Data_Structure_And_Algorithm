class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.root = None

    def isEmpty(stack):
        return True if stack.root is None else False

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.root
        self.root = new_node
        print("%d pushed to stack" %(new_data))

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        print("%d popped from stack" %(temp.data))
    
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        print("%d is stack top element"%(self.root.data))

stack=Stack()
stack.push(10)
stack.push(11)
stack.push(12)
stack.push(13)

stack.pop()
stack.peek()



# 10 pushed to stack
# 11 pushed to stack
# 12 pushed to stack
# 13 pushed to stack
# 13 popped from stack
# 12 is stack top element
