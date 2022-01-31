from sys import maxsize

def createstack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(self, item):
    self.append(item)

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize -1)
    return stack.pop()

def insertatbottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertatbottom(stack, item)
        push(stack, temp)

def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertatbottom(stack,temp)

def printstack(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=" ")
    print()


stack = createstack()
push(stack, str(10))
push(stack, str(11))
push(stack, str(12))
print("Original stack:")
printstack(stack)
print("Reversed stack:")
reverse(stack)
printstack(stack)



# Original stack:
# 12 11 10 
# Reversed stack:
# 10 11 12 