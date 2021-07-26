def traversematrix(arr,r,c):
    for i in range(r):
        for j in range(c):
            print(arr[i][j],end = " ")
        print()
            
            
# arr=[ [1,2,3],[4,5,6],[7,8,9]]
# traversematrix(arr,3,3)

def searchingInMatrix(arr,r,c,key):
    flag = False
    for i in range(r):
        for j in range(c):
            if arr[i][j] == key:
                flag = True
    
    if flag == True:
        return("Element is present")
    return("No such Element")

# arr=[ [1,2,3],[4,5,6],[7,8,9]]
# print(searchingInMatrix(arr,3,3,13))

##########################################################
# Addition of two matrix
N = 4
def add(A,B,C):
 
    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j] + B[i][j]
            
A = [ [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]
  
B= [ [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4]]
  
C=A[:][:] # To store result
 
# add(A, B, C)
# traversematrix(C,4,4)

#########################################################
# multiplication of matrix:

def multiplyMatrix(m1, m2, mat1,n1, n2, mat2):

	res = [[0 for x in range(n2)]
			for y in range (m1)]
	
	for i in range(m1):
		for j in range(n2):
			res[i][j] = 0
			for x in range(m2):		
				res[i][j] += (mat1[ i][x] * mat2[ x][j])
			
	for i in range(m1):
		for j in range(n2):	
			print (res[i][j],
				end = " ")	
		print ()
    


# mat1 = [[2, 4], [3, 4]]
# mat2 = [[1, 2], [1, 3]]
# m1, m2, n1, n2 = 2, 2, 2, 2

# multiplyMatrix(m1, m2, mat1,n1, n2, mat2)
##################################################################

# Python3 program to rotate a matrix by 90 degrees
N = 4

# An Inplace function to rotate N x N matrix by 90 degrees in anti-clockwise direction
def rotateMatrix(mat):

	for x in range(0, int(N / 2)):
		
		# Consider elements in group of 4 in current square
		for y in range(x, N-x-1):
			

			temp = mat[x][y]

			# move values from right to top
			mat[x][y] = mat[y][N-1-x]

			# move values from bottom to right
			mat[y][N-1-x] = mat[N-1-x][N-1-y]

			# move values from left to bottom
			mat[N-1-x][N-1-y] = mat[N-1-y][x]

			# assign temp to left
			mat[N-1-y][x] = temp


# Function to print the matrix
def displayMatrix( mat ):
	
	for i in range(0, N):
		for j in range(0, N):
			print (mat[i][j], end = ' ')
		print ("")

# Driver Code
mat = [[0 for x in range(N)] for y in range(N)]

# Test case 1
mat = [ [1, 2, 3, 4 ],
		[5, 6, 7, 8 ],
		[9, 10, 11, 12 ],
		[13, 14, 15, 16 ] ]
		
'''
# Test case 2
mat = [ [1, 2, 3 ],
		[4, 5, 6 ],
		[7, 8, 9 ] ]

# Test case 3
mat = [ [1, 2 ],
		[4, 5 ] ]
		
'''

# rotateMatrix(mat)
# displayMatrix(mat)

###################################################################
m=3
n=4
def transpose(a,b):
    for i in range(n):
        for j in range(m):
            b[i][j]= a[j][i]
    return b

b =[[ 0 for i in range(m)] for j in range(n)]
a = [ [1, 4, 7, 1],
    [2, 5, 8, 2],
    [3, 6, 9, 3]]

# x=transpose(a,b)
# traversematrix(x,n,m)

 ####################################################################
 #spiral of matrix

def spiralPrint(m, n, arr):
	k = 0
	l = 0

	while (k < m and l < n):
		for i in range(l, n):
			print(a[k][i], end=" ")

		k += 1

		for i in range(k, m):
			print(a[i][n - 1], end=" ")

		n -= 1

		if (k < m):

			for i in range(n - 1, (l - 1), -1):
				print(a[m - 1][i], end=" ")

			m -= 1

		if (l < n):
			for i in range(m - 1, k - 1, -1):
				print(a[i][l], end=" ")

			l += 1

a = [[1, 2, 3, 4, 5, 6],
	[7, 8, 9, 10, 11, 12],
	[13, 14, 15, 16, 17, 18]]

R = 3
C = 6

# Function Call
spiralPrint(R, C, a)
#
"""Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence 
of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s 
(0 based indexing)."""


      
    
    
    
    
    
    
    