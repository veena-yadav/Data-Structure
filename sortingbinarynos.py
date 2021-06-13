# Sort an array of 0s, 1s and 2s



def sortarr(arr,n):
    
    cnt = 0 
    cnt1 =0
    cnt2 = 0
    for i in range(n):
        if arr[i] ==0:
            cnt += 1
        elif arr[i]==1:
            cnt1 += 1
        elif arr[i] ==2:
            cnt2 += 1
            
    for i in range(0,cnt):
        arr[i]=0
            
    for i in range(cnt, (cnt + cnt1)):
        arr[i] = 1

    for i in range((cnt + cnt1), n):
        arr[i] = 2
    
    return 

def printArray( arr,  n):
 
    for i in range(0,n):
        print( arr[i] , end=" ")
    print()


arr = [ 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 ]
n = len(arr)
sortarr(arr, n)
printArray(arr, n)