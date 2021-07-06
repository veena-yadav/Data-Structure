#https://github.com/NEERAJAP2001/DSA-Python
# Recursive method
def ReverseArray(arr, start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    print(arr)
    
# arr =[1,2,3,4,5,6,7,8]
# print(arr)
# print('Reverse array')
# ReverseArray(arr,0,7) 


# two line code of reversing a array
def reverseList(A):
  print( A[::-1])
     
# arr =[1,2,3,4,5,6,7,8]
# print(arr)
# print('Reverse array')
# reverseList(arr)

# Reverse a array only one step ahead
def rotate(arr, n):
    x = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = x

def rotateNTime(arr, d, n):
    for i in range(d):
        rotate(arr, n)
    return arr   

# arr = [1,2,3,4,5]
# n = len(arr)
# print(rotateNTime(arr,3,n))
