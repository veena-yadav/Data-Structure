# Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

n = int(input())
l = list(map(int,input().split()))
k = int(input())

l.sort()
ls = l
def printkth(ls):
    return ls[k-1]
    
print(printkth(ls))