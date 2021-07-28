# Given an array of integers of size 'n'.
# Our aim is to calculate the maximum sum of 'k' 
# consecutive elements in the array.

def maxSum(arr,k):
    n = len(arr)
    windowSum = sum(arr[:k])
    # print(windowSum)
    if n < k:
        print("Invalid")
        return -1
    
    max_sum = windowSum
    for i in range(n-k):
        windowSum = windowSum + arr[i+k] - arr[i]
        # print(windowSum)
        max_sum = max(windowSum, max_sum)
    return max_sum
    
    
# Driver code
arr = [1, 4, 2, 20, 2, 3, 1, 0, 20]
k = 2
print(maxSum(arr, k))