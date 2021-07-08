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
# print(RangeCoff(arr))
        

##########################################################################
# You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates 
# in the list. One of the integers is missing in the list.

def MissingNum(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return int(total - sum_of_A)
    # arr.sort()
    # flag =0
    # for i in range(1,n):
    #     if arr[i] - arr[i-1] != 1:
    #         x = arr[i] + 1
    #         flag =0
    #     else:
    #         flag = 1
            
    # if flag == 1:
    #     return("no elment is missing")
    # return x
        
arr = [1, 2, 4, 6, 3, 7, 8]
# print(MissingNum(arr))

################################################################3
# Count pairs with given sum

def Countpairs(arr,Sum_given):
    n = len(arr)
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == Sum_given:
                cnt += 1
                
    return cnt

arr = [1, 5, 7, -1, 5]
print(Countpairs(arr,6))

##############################################################33

numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
n = len(numRay)
for i in range(n):

	x = numRay[i] % n
	numRay[x] = numRay[x] + n

print("The repeating elements are : ")
for i in range(n):
	if (numRay[i] >= n*2):
		print(i, " ")

####################################################################

def findCommon(ar1,ar2,ar3,n1,n2,n3):
    i, j, k = 0, 0, 0
    while(i<n1 and j<n2 and k<n3):
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print(ar1[i])
            i += 1
            j += 1
            k += 1
        
        elif ar1[i]<ar2[j]:
            i += 1
        elif ar2[j]< ar3[k]:
            j += 1
        else:
            k += 1
        
    
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
print("Common elements are")
findCommon(ar1, ar2, ar3, n1, n2, n3)


















