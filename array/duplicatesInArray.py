def Duplicates(arr):
    arr.sort()
    for i in range(0,len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]
        
        
arr = [1,2,3,4,5,5]
# print(Duplicates(arr))

# n = 4, m = 5
# arr1[] = {1, 3, 5, 7}
# arr2[] = {0, 2, 6, 8, 9}

# def mergeSortedArr(arr1,arr2,n,m):
#     for i in 


# Search a elment in arrary
arr1 = [12, 34, 10, 6, 40]
n = len(arr)
def SearchArr(arr,n,x):
    for i in range(n):
        if arr[i]==x:
            return i
    return("element does not exit")
    
print(SearchArr(arr1,n,34))