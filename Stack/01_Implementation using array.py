from sys import maxsize

def createstack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(self, item):
    self.append(item)
    print( item +' pushed in stack')

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize -1)
    return stack.pop()

def peek(stack):
    if isEmpty(stack):
        return str(-maxsize -1)
    return stack[len(stack) -1]

stack = createstack()
push(stack, str(10))
push(stack, str(11))
push(stack, str(12))
print(pop(stack) + " popped from stack")



# 10 pushed in stack
# 11 pushed in stack
# 12 pushed in stack
# 12 popped from stack
