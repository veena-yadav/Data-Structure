# Sort an array of 0s, 1s and 2s

arr = [0,1,0,2,0,1,2]


def sortarr(arr):
    n = len(arr)
    l = []
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
            
        while cnt > 0:
            l.append(0)
            cnt -= 1
        
        while cnt > 0:
            l.append(1)
            cnt -= 1
        
        while cnt2 > 0:
            l.append(2)
            cnt -= 1
    
    return l

ls = sortarr(arr)
print(ls)