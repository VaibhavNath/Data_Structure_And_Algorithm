def rotate(arr, n):
    x = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = x


arr = [1,2,3,4,5,6,7]
n = len(arr)
print("given array is: ")
for i in range(0, len(arr)):
        print(arr[i], end=" ")

rotate(arr, n)
print("\narray after rotation is:")
for i in range(0, len(arr)):
        print(arr[i], end=" ")



# given array is: 
# 1 2 3 4 5 6 7 
# array after rotation is:
# 7 1 2 3 4 5 6 