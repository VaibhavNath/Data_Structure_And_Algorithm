def reverseArray(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start +=1
        end = end-1

def leftrotate(arr, d):
    if d == 0:
        return 
    n = len(arr)
    d =d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)

def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=" ' ")

arr = [1,2,3,4,5,6]
n=len(arr)
d=2
leftrotate(arr, d)
print(arr)


# [3, 4, 5, 6, 1, 2]