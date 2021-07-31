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

display_hash (HashTable)
