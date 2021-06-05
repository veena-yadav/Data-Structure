# Recursive method
def ReverseArray(arr, start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    print(arr)
    
arr =[1,2,3,4,5,6,7,8]
print(arr)
print('Reverse array')
ReverseArray(arr,0,7) 


# two line code of reversing a array
# def reverseList(A):
#   print( A[::-1])
     
# arr =[1,2,3,4,5,6,7,8]
# print(arr)
# print('Reverse array')
# reverseList(arr)

