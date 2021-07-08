# Problem #2 : Equilibrium index of an array

def calEquillibrium(arr,n):
   
    for i in range(0,n):
        leftsum = 0
        rightsum = 0
        for x in range(0,i):
            leftsum += arr[x] 
        for x in range(i+1,n):
            rightsum += arr[x]  
        
        if leftsum == rightsum:
            return i
    return -1
    
    
arr = [-7, 1, 5, 2, -4, 3, 0]
n = len(arr)
print (calEquillibrium(arr,n))