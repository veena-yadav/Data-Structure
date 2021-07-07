# Move all negative numbers to beginning and positive to end with constant extra space

def NegativeSideInArray(arr, n):
    cnt1 = 0
    l = []
    for i in range(0,n):
        if arr[i] < 0:
            l.append(arr[i])
        else:
            cnt1 += 1
            
            
    for i in range(n):
        if arr[i] > 0:
            l.append(arr[i])
            
    return l

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
ls = NegativeSideInArray(arr,n)
print(ls)
        