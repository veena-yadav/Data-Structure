# Union  of array

a1 = [1, 2, 3, 4, 5]
a2 = [1, 2, 3]
m = len(a1)
n = len(a2)
# a1.extend(a2)
# ls = set(a1)

# cnt = len(ls)
# print(cnt)

# # Intersection with arrary

# for i in a2:
#     if i not in a1:
#         a1.remove(i)
        
# print(a1)

def unionarr(a1,a2, m,n):
    i=0
    j=0
    while i<m and j<n:
        if a1[i]<a2[j]:
            print(a1[i])
            i+= 1
            
        elif a2[j]<a2[i]:
            print(a2[j])
            j += 1
            
        else:
            print(a2[j])
            i += 1
            j += 1
            
    while i< m:
        print(a1[i])
        i += 1
        
    while j<n:
        print(a2[i])
        j += 1
        
# unionarr(a1, a2, m, n)

def intersectioarr(a1,a2,m,n):
    for i in a2:
        if x in a1:
            pass
        else:
            print(a2[i])
            
intersectioarr(a1, a2, m, n)