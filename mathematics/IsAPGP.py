def IsAP(arr):
    arr.sort()
    d = arr[1]-arr[0]
    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]!= d:
            return("no it is a Ap")
    return("yes it is a Ap")
    
        
#arr=[ 20, 15, 5, 0, 10 ]
# print(IsAP(arr))

def IsGP(arr):
    arr.sort()
    r = arr[1]/arr[0]
    for i in range(2,len(arr)):
        if arr[i]/arr[i-1] != r:
            return("no it is a Gp")
    return("yes it is a Gp")

arr=[2, 6, 18, 64]
arr=[2, 6, 18, 54]
# print(IsGP(arr))

