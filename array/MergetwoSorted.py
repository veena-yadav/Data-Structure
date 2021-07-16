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

# arr = [1, 5, 7, -1, 5]
# print(Countpairs(arr,6))

##############################################################33

numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
n = len(numRay)
for i in range(n):

	x = numRay[i] % n
	numRay[x] = numRay[x] + n

# print("The repeating elements are : ")
# for i in range(n):
# 	if (numRay[i] >= n*2):
# 		print(i, " ")

####################################################################
"""
Find common elements in three sorted arrays
Input: 
ar1[] = {1, 5, 10, 20, 40, 80} 
ar2[] = {6, 7, 20, 80, 100} 
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
Output: 20, 80

Input: 
ar1[] = {1, 5, 5} 
ar2[] = {3, 4, 5, 5, 10} 
ar3[] = {5, 5, 10, 20} 
Output: 5, 5"""
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
        
    
# ar1 = [1, 5, 10, 20, 40, 80]
# ar2 = [6, 7, 20, 80, 100]
# ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
# n1 = len(ar1)
# n2 = len(ar2)
# n3 = len(ar3)
# print("Common elements are")
# findCommon(ar1, ar2, ar3, n1, n2, n3)


####################################################################
"""Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest. """

def printFirstRepeating(arr,n):
    # for i in range(n):
    #     if arr.count(arr[i])>1:
    #         return arr[i]
    # return "not exist"
    
    # Method 2
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return(arr[i])
              
          
    

# arr = [6, 10, 5, 4, 9, 120, 4, 6, 10]
# n = len(arr)
# print(printFirstRepeating(arr, n))

###############################################################33

# Non-Repeating Element
def NonRepeatingfirstNo(arr,n):
    for i in range(n):
        j =0
        while(j<n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
            
        if j == n:
            return arr[i]
    return -1

# Driver code
# arr = [ 9, 4, 9, 6, 7, 4 ]
# n = len(arr)
# print(NonRepeatingfirstNo(arr, n))

#################################################################3333333

# Find the largest three distinct elements in an array


# Driver program to test above function
arr = [12, 45, 1, -1, 45,
       54, 23, 5, 0, -10]

arr1 = set(arr)
arr = list(arr1)
arr.sort(reverse= True)

# for i in range(3):
    # print(arr[i])

############################################################################

# Rearrange array in alternating positive & negative items

def Rearrange(arr,n):
    arr.sort()
    i, j = 1, 1
    while j < n:
        if arr[j] > 0:
            break
        j += 1
 
    while (arr[i] < 0) and (j < n):
        
        arr[i], arr[j] = arr[j], arr[i]  
         
        # increment i by 2
        # because a negative number is followed by a positive number
        i += 2     
        j += 1
     
    return(arr)

# arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
 
# ans = Rearrange(arr, len(arr))
# for num in ans:
#     print(num, end = " ")


###########################################################

def maxSubarrayProduct(arr, n):

    result = arr[0]
 
    for i in range(n):
     
        mul = arr[i]
        for j in range(i + 1, n):
            result = max(result, mul)
            mul *= arr[j]
        result = max(result, mul)
     
    return result

# arr = [ 1, -2, -3, 0, 7, -8, -2 ]
# n = len(arr)
# print("Maximum Sub array product is" , maxSubarrayProduct(arr, n))

############################################################################

#Longest Consecutive Subsequence

def longestSequence(arr, n):
    arr.sort()
    x =[]
    x.append(arr[0])
    for i in range(1,n):
        if arr[i] == arr[i-1] + 1:
            x.append(arr[i])
        
        if arr[i] != arr[i-1] + 1:
            break
    
    return x

# arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
# n = len(arr)
# print(longestSequence(arr,n))

#############################################################################3

# minimum element in a sorted and rotated array contating duplicate elements.
 
# Function to find minimum element
def findMin(arr, low, high):
   
    while (low < high):
        mid = low + (high - low) // 2
         
        if(arr[mid] == arr[high]):
            high -= 1
        elif(arr[mid] > arr[high]):
            low = mid + 1
        else:
            high = mid
    return arr[high]

# arr1 = [5, 6, 1, 2, 3, 4]
# n1 = len(arr1)
# print("The minimum element is ",findMin(arr1, 0, n1 - 1))

###################################################################################

# Minimize the maximum difference between the heights

def findmaxDif(arr,n,k):
    arr.sort()
    ans = arr[n-1] - arr[0]
    small = large = 0
    
    for i in range(1,n):
        small = min(arr[0] + k, arr[i]-k)
        large = max(arr[i-1]+k,arr[-1]-k)
        ans = min(ans, large- small)

    return ans

# arr=[1, 5, 15, 10]
# k=3
# print(findmaxDif(arr,len(arr),k))
##############################################################################################
""" Find a triplet that sum to a given value
Input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
Output: 12, 3, 9 
"""
def findTriplet(arr,n,sum):
    for i in range( 0, n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                if A[i] + A[j] + A[k] == sum:
                    print("Triplet is", A[i],
                          ", ", A[j], ", ", A[k])
                    return True
    
# A = [1, 4, 45, 6, 10, 8]
# sum = 22
# n = len(A)
# print(findTriplet(A, n, sum))

###################################################################33333
def rowWithMax1s( mat):
      
    # Initialize max values
    R = len(mat)
    C = len(mat[0])
    max_row_index = 0
    index=C-1
    # Traverse for each row and
    # count number of 1s by finding
    # the index of first 1
    for i in range(0, R):
      flag=False 
      while(index >=0 and mat[i][index]==1):
        flag=True 
        index-=1
        if(flag): 
          max_row_index = i
      if max_row_index==0 and mat[0][C-1]==0:
        return 0
    return max_row_index
arr = [[0, 0, 0, 1],
       [0, 0, 1, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1]]

# print(rowWithMax1s(arr))

###############################################################
# Python3 program to print
# given matrix in spiral form


def spiralPrint(m, n, a):
	k = 0
	l = 0

	''' k - starting row index
		m - ending row index
		l - starting column index
		n - ending column index
		i - iterator '''

	while (k < m and l < n):

		# Print the first row from
		# the remaining rows
		for i in range(l, n):
			print(a[k][i], end=" ")

		k += 1

		# Print the last column from
		# the remaining columns
		for i in range(k, m):
			print(a[i][n - 1], end=" ")

		n -= 1

		# Print the last row from
		# the remaining rows
		if (k < m):

			for i in range(n - 1, (l - 1), -1):
				print(a[m - 1][i], end=" ")

			m -= 1

		# Print the first column from
		# the remaining columns
		if (l < n):
			for i in range(m - 1, k - 1, -1):
				print(a[i][l], end=" ")

			l += 1



a = [[1, 2, 3, 4, 5, 6],
	[7, 8, 9, 10, 11, 12],
	[13, 14, 15, 16, 17, 18]]

R = 3
C = 6

spiralPrint(R, C, a)

