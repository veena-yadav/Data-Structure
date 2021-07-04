def find_water_fill(arr, n):
    total_water = 0
    for i in range(n):
        leftMax = LeftMax(arr,n,i)
        rightMax = RightMax(arr,n,i)
        total_water = total_water + min(leftMax,rightMax) - arr[i]
        
    return total_water
    
def LeftMax(arr, n, i):
    maximum = 0
    for i in range(0,i):
        maximum = max(maximum,arr[i])
    return maximum

def RightMax(arr, n, i):
    maximum = 0
    for i in range(i,n):
        maximum = max(maximum,arr[i])
    return maximum

a = [1,2,1]
print(find_water_fill(a,len(a)))