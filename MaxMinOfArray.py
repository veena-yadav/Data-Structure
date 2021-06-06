# #Maximum and minimum of an array using minimum number of comparisons

arr= [1,5,8,6,10]
def maxMin(arr):
    max = arr[0]
    min = arr[0]
    for i in range(len(arr)):
        if max <= arr[i]:
            max= arr[i]
    
        if min >= i:
            min= arr[i]
    print('max',max)
    print('min',min)

maxMin(arr)

# To calculate max
# arr= [1000, 11, 445, 1, 330, 3000]
# def max(arr):
#     max= arr[0]
#     for i in range(len(arr)):
#         if max <= arr[i]:
#             max= arr[i]
#     return max

# print('max number: ',max(arr))

# # # To calculate min
# arr= [1000, 11, 445, 1, 330, 3000]
# def max(arr):
#     min= arr[0]
#     for i in range(len(arr)):
#         if min >= i:
#             min= arr[i]
           
#     return min

# print('minimun number: ' , min(arr))