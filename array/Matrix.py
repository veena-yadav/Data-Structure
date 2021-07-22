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