# prefix array sum


def arrSum(arr):
    l = []
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        l.append(sum)
       
    return l

# arr = [10, 20, 10, 5, 15]
# print(arrSum(arr))

#####################################################
def prefixSum(arr,j,k):
    l = len(arr)
    for i in range(1, l):
        ans = sum(arr[j:k+1])
    print(ans)
    return
    
pr = [1, 2, 3, 4, 5]
ar = pr[:]
prefixSum(ar, 1, 3)
ar = pr[:]
prefixSum(ar, 2, 4)
# arr = list(input().split(" "))
# n = int(input())

# for i in range(n):
#     x, y = [int(x) for x in input().split()]
    
    
# print(prefixSum( arr,y,x))