def MergeTwoSorted(arr1,arr2):
    arr1.extend(arr2)
    arr1.sort()
    print(arr1)

# arr1 = [1, 3, 4, 6]
# arr2 = [2, 5, 7, 8]

# MergeTwoSorted(arr1,arr2)


def SecondMethod(arr1,arr2,n,m):
    arr = []
    i =0
    j =0
    while i<m and j<n:
        if arr1[i]< arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
            
    while i< n:
        arr.append(arr1[i])
        i += 1
    while j< m:
        arr.append(arr2[j])
        j += 1
    return arr
        
# arr1 = [1, 3, 4, 6]
# arr2 = [2, 5, 7, 8]

# print(SecondMethod(arr1,arr2,len(arr1),len(arr2)))