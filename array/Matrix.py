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

def multiplyMatrix(m1, m2, mat1,
			n1, n2, mat2):

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
    


mat1 = [[2, 4], [3, 4]]
mat2 = [[1, 2], [1, 3]]
m1, m2, n1, n2 = 2, 2, 2, 2

multiplyMatrix(m1, m2, mat1,n1, n2, mat2)
	


    
    
    
    
    
    
    
    