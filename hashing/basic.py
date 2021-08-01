# Chaining
# While hashing, the hashing function may lead to a collision that is two or more keys are mapped to the same value. Chain hashing avoids collision.
# The idea is to make each cell of hash table point to a linked list of records that have same hash function value.


# linear probing: aagr slot khali na ho 1 no. aage jayega free h to wha daal dega.
# prob no kitn baar aage bade apni actual no se.
# searching time O(1) normal, worst O(n)
# (hash(x) + i) % S

# quardratic probabing quardatic nature se chalega aagr collision hua to.
# distadvantage guarantee nahi h jgh mil payegi elment dalne ke liye kayi baar jgh khali hogi pr tquartic nature ki wjh se nhi milegi.
# O(n) second clustering hosakti h primary nhi
# (hash(x) + i*i) % S 

# Double Hashing We use another hash function hash2(x) and look for i*hash2(x) slot in i'th rotation
# Double hashing has poor cache performance but no clustering. Double hashing requires more computation time as two hash functions need to be computed.


# Function to display hashtable
def display_hash(hashTable):
	
	for i in range(len(hashTable)):
		print(i, end = " ")
		
		for j in hashTable[i]:
			print("-->", end = " ")
			print(j, end = " ")
			
		print()

# Creating Hashtable as
# a nested list.
HashTable = [[] for _ in range(10)]

# Hashing Function to return
# key for every value.
def Hashing(keyvalue):
	return keyvalue % len(HashTable)


# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
	
	hash_key = Hashing(keyvalue)
	Hashtable[hash_key].append(value)

# Driver Code
insert(HashTable, 10, 'Allahabad')
insert(HashTable, 25, 'Mumbai')
insert(HashTable, 20, 'Mathura')
insert(HashTable, 9, 'Delhi')
insert(HashTable, 21, 'Punjab')
insert(HashTable, 21, 'Noida')

# display_hash (HashTable)


###################################################
# via linear probing

def printHash(hashtable):
    for i in range(len(hashtable)):
        print(i, end=" ")
        for j in hashtable[i]:
            print("--->", end=" ")
            print(j, end=" ")
            
        print()
        
HashTable = [[] for _ in range(10)]

def generatekey(value):
    return value % len(HashTable)

def insertinHash(hashtable,value,data):
    hashKey = generatekey(value)
    HashTable[hashKey].append(data)
    
    
###############################################
# Efficient Python program to print all non-
# repeating elements.

def firstNonRepeating(arr, n):

	mp={}
	for i in range(n):
		if arr[i] not in mp:
			mp[arr[i]]=0
		mp[arr[i]]+=1
		# print(mp)
	# Traverse through map only and
	for x in mp:
		if (mp[x]== 1):
			print(x,end=" ")
			

# arr = [ 9, 4, 9, 6, 7, 4 ]
# n = len(arr)
# firstNonRepeating(arr, n)

##################################################################
def maxDistance( arr, n):
        mp = {}
        maxDict = 0
        
        for i in range(n):
    
            if arr[i] not in mp.keys():
                mp[arr[i]] = i
            else:
                maxDict = max(maxDict, i-mp[arr[i]])
     
        return maxDict
    
# arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
# print( maxDistance(arr, len(arr)))

#######################################################
#Given an array of integers, sort the array according to frequency of elements. That is elements that have higher frequency 
# come first. If frequencies of two elements are same, then smaller number comes first.
def sortByFreq(a,n):
    from collections import defaultdict
        
    d = defaultdict(lambda: 0)
    for i in range(n):
        d[a[i]] += 1
        print(d)
     
    a.sort(key=lambda x: (-d[x], x))
    return (a)

# a=[5,5,4,6,4]
# print(sortByFreq(a,len(a)))

###############################################################
def topK(nums, k):
		
	mp = {}
	l =[]
	for i in range(len(nums)):
		if nums[i] not in mp:
		    mp[nums[i]]=0
		mp[nums[i]] +=1
		    
	for x in mp:
	    if mp[x]==k:
	        l.append(x)
	            
	l.sort()
	return l
# a=[5,5,4,6,4]
# print(topK(a,2))
############################################################
# def topK(nums, k):
	
# 	mp = {}
# 	l =[]
# 	for i in range(len(nums)):
# 		if nums[i] not in mp:
# 		    mp[nums[i]]=0
# 		mp[nums[i]] +=1
# 	a = [0] * (len(mp))
# 	j = 0
# 	for i in mp:
#     	a[j] = [i, mp[i]]
#     	j += 1
#     	a = sorted(a, key=lambda x: x[0],
#                    reverse=True)
#     	a = sorted(a, key=lambda x: x[1],
#                    reverse=True)
# 	for i in range(k):
#         l.append(a[i][0])
#         return l

#############################################################
def insert(dict, key, value):
    dict.setdefault(key, []).append(value)
 
def printallSublists(A):

    dict = {}
    insert(dict, 0, -1)
 
    sum = 0
    count =0
    for i in range(len(A)):
 
        sum += A[i]

        if sum in dict:

            list = dict.get(sum)
 
            # find all sublists with the same sum
            for value in list:
                print("Sublist is position", (value + 1, i))
                count +=1
        # insert (sum so far, current index) pair into the dictionary
        insert(dict, sum, i)
    print("total subarray who has sum 0 are: ",count)
    
 
 
# if __name__ == '__main__':
 
#     A = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
 
#     printallSublists(A)