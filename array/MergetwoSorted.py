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
# Python 3 program to find
# the every segment size of
# array have a search key x

def findxinkindowSize(arr, x, k, n) :
    # for i in range(0,n-1,k):
    #     for j in range(0,k,1):
    #         if arr[i + j] == x :
    #             break
        
    #     if j == k:
    #         return False
        
    # if i == n :
    #     return True
	i = 0
	while i < n :
		j = 0
		# Search x in segment starting from index i
		while j < k :
			if arr[i + j] == x :
				break
			j += 1

		# If loop didn't break
		if j == k :
			return False

		i += k
		
	# If n is a multiple of k	
	if i == n :
		return True

	j = i - k
	
	# Check in last segment if n is not multiple of k.
	while j < n :
		if arr[j] == x :
			break
		j += 1

	if j == n :
		return False

	return True

# Driver Code
# if __name__ == "__main__" :
 
#     arr = [21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]
#     x, k = 23, 5
#     n = len(arr)
     
#     if (findxinkindowSize(arr, x, k, n)) :
#         print("Yes")
#     else :
#         print("No")

# arr[] = { 5, 8, 7, 12, 14, 3, 9} 
# x = 8 
# k = 2 


####################################################################
#Range and Coefficient of range of Array
# Range=> max-min
# cofficient => max-min/ max+min

def RangeCoff(arr):
    mx = max(arr)
    mn = min(arr)
    
    range = mx - mn
    cofficient = (mx - mn)/(mx + mn)
    return (range,cofficient)

arr = [15, 16, 10, 9, 6, 7, 17]
print(RangeCoff(arr))
        























