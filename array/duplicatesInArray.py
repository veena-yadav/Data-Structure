def Duplicates(arr):
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]
        
        
arr = [1,2,3,4,5,5]
# print(Duplicates(arr))

#####################################

# Search a elment in arrary
arr1 = [12, 34, 10, 6, 40]
n = len(arr)
def SearchArr(arr,n,x):
    for i in range(n):
        if arr[i]==x:
            return i
    return("element does not exit")
    
# print(SearchArr(arr1,n,34))

############################################

# count frequency of element in a sorted arrray
arr1 = [12, 34, 10,12,12, 6, 40]
n = len(arr)
def countfreq(arr,n,x):
    count = 0
    arr.sort()
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count
    # return("element does not exit")
    
# print(countfreq(arr1,n,12))