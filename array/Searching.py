def binarySearch(arr,left,right,x):
    
    if right >= left:
        mid= left + (right-1)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr,left,mid-1,x)
        else:
            return binarySearch(arr,mid+1,right,x)
    else:
        return -1
    
arr = [2,5,8,12,16,23,38,56,72,91]
n= len(arr)   
result = binarySearch(arr,0,n-1,10)

if result != -1:
    print ("Element is present at index % d" % result)
else:
    print ("Element is not present in array")
    