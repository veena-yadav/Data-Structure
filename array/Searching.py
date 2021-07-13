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

############################################################################
"""
x = 5
Output: 2
Explanation: Since, 5 is not a perfect 
square, floor of square_root of 5 is 2.

"""
def floorSqrt(self, x): 
    #Your code here
        if x ==0 and x ==1:
            return x
        
        i = 1
        res = 0
        
        while res <= x:
            i += 1
            res = i*i
        return i-1
    
#############################################################################
"""N = 3
arr[] = {1,2,3}
Output: 1"""
def peakElement(self,arr, n):

        if n==1:
            return 0
        if arr[0] >= arr[1]:
            return 0
        if arr[n-1] >= arr[n-2]:
            return n-1
            
        for i in range(1,n-1):
            if (arr[i]>= arr[i-1] and arr[i]>= arr[i+1]):
                return i
            
#########################################################################

# find element in sorted and rotated arrary
def Search(arr,n,k):
    #code here
    pivot = findPivot(arr, 0, n-1)
 
    if pivot == -1:
        return binarySearch(arr, 0, n-1, k)

    if arr[pivot] == k:
        return pivot
    if arr[0] <= k:
        return binarySearch(arr, 0, pivot-1, k)
    return binarySearch(arr, pivot + 1, n-1, k)
 
 
def findPivot(arr, low, high):
     
    # base cases
    if high < low:
        return -1
    if high == low:
        return low
     
    mid = int((low + high)/2)
     
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid + 1, high)
 

def binarySearch(arr, low, high, k):
 
    if high < low:
        return -1
         
    mid = int((low + high)/2)
     
    if k == arr[mid]:
        return mid
    if k > arr[mid]:
        return binarySearch(arr, (mid + 1), high,k)
    return binarySearch(arr, low, (mid -1), k)
 