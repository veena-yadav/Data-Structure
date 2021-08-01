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
    
# pr = [1, 2, 3, 4, 5]
# ar = pr[:]
# prefixSum(ar, 1, 3)
# ar = pr[:]
# prefixSum(ar, 2, 4)
# arr = list(input().split(" "))
# n = int(input())

# for i in range(n):
#     x, y = [int(x) for x in input().split()]
    
    
# print(prefixSum( arr,y,x))

"""Input
n= 6
arr = {1, 1, 2, 2, 2, 1}

Output
5

Explanation
arr[] = {1, 1, 2, 2, 2, 1}
Max Distance: 5
Distance for 1 is: 5-0 = 5
Distance for 2 is : 4-2 = 2
Max Distance 5"""
def maxDistance(arr, n):
    x = arr[n-1]
    for i in range(n):
        if arr[i] == x:
            return int(n-i-1)
        
a = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
# print(maxDistance(a,len(a)))

def maxLen(arr):
    #Code here
    # maxlen = 0
    # for i in range(n):
    #     cursum = 0
    #     for j in range(i,n):
    #         cursum += arr[j]
    #         if cursum == 0:
    #             maxlen = max(maxlen , j-i+1)
    # return maxlen
    # o(n^^2) time complexity
    
    
    # 2nd method witho(n)
    hash_map = {}

    max_len = 0
    curr_sum = 0

    for i in range(len(arr)):
         
        curr_sum += arr[i]
 
        if arr[i] is 0 and max_len is 0:
            max_len = 1
 
        if curr_sum is 0:
            max_len = i + 1
 
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum] )
        else:
            hash_map[curr_sum] = i
 
    return max_len

"""Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7."""