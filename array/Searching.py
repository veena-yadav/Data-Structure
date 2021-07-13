# O(Log N), where N is the number of elements in the array.
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

# if result != -1:
#     print ("Element is present at index % d" % result)
# else:
#     print ("Element is not present in array")
    
########################################################################################3
def insertionSort(arr):

    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr
 

# arr = [12, 11, 13, 5, 6]
# print(insertionSort(arr))
###########################################################

def bubllesort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j], 
                
    return arr

# arr = [12, 11, 13, 5, 6]
# print(bubllesort(arr))
#################################################################
#partition

def partition(start,end,arr):
    pivotIndex = start
    pivot  = arr[pivotIndex]
    
    while start<end:
        while start <len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    
    arr[end], arr[pivotIndex] = arr[pivotIndex], arr[end]
    return end

def quick_sort(start, end, arr):
     
    if (start < end):
    
        p = partition(start, end, arr)

        quick_sort(start, p - 1, arr)
        quick_sort(p + 1, end, arr)

# arr = [ 10, 7, 8, 9, 1, 5 ]
# quick_sort(0, len(arr) - 1, arr)
# print(f'Sorted array: {arr}')
    
############################################################3333333333333

def Mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        
        l = arr[:mid]
        r = arr[mid:]
        
        Mergesort(l)
        Mergesort(r)
        
        i = j= k = 0
        
        while i<len(l) and j <len(r):
            if l[i] < r[i]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
                
            k += 1

        while i <len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j <len(r):
            arr[k] = r[j]
            j += 1
            k += 1   
        
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(Mergesort(arr))