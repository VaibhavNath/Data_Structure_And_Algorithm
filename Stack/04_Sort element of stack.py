def sortedInsert(S, element):
    if len(S)==0 or element > S[-1]:
        S.append(element)
        return

    else:
        temp = S.pop()
        sortedInsert(S, element)
        S.append(temp)

def Sortstack(S):
    if len(S) != 0:
        temp = S.pop()
        Sortstack(S)
        sortedInsert(S,temp)

def printStack(s):
    for i in s[::-1]:
        print(i, end=" ")
    print()

if __name__ == '__main__':
    s = []
    s.append(30)
    s.append(-5)
    s.append(18)
    s.append(14)
    s.append(-3)
 
    print("Stack elements before sorting: ")
    printStack(s)
 
    Sortstack(s)
 
    print("\nStack elements after sorting: ")
    printStack(s)



# Stack elements before sorting: 
# -3 14 18 -5 30 

# Stack elements after sorting: 
# 30 18 14 -3 -5 