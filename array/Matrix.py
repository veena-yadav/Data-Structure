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