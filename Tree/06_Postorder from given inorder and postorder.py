class Node:
    def __init__(self, key):
        self.data = key 
        self.left = None
        self.right = None

def search(arr, x, n):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

def printpostorder(ino, preo, n):
    
    #first element in preorder is always root, search it in search[] to find left and right subtree
    root = search(ino, preo[0], n)

    #if left subtree is not empty print left subtree
    if root != 0:
        printpostorder(ino, preo[1:n], root)

    #if right subtree is not empty print right subtree
    if root != n-1 :
        printpostorder(ino[root+1:n], preo[root+1:n], n-root-1)
    
    print(preo[0],end =" ")


ino=[4,2,5,1,3,6]
preo=[1,2,4,5,3,6]
n=len(ino)
printpostorder(ino, preo, n)         # 4 5 2 6 3 1 