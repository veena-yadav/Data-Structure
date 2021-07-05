# Python program to demonstrate Basic Euclidean Algorithm
# Function to return gcd of a and b

def gcd(a, b):
    if a == 0 :
        return b
     
    return gcd(b%a, a)
 
a = 10
b = 15
print("gcd(", a , "," , b, ") = ", gcd(a, b))

# Python3 program to find LCM of array

def LCM(arr, n):
	
	# Find the maximum value in arr[]
	max_num = 0
	for i in range(n):
		if (max_num < arr[i]):
			max_num = arr[i]

	# Initialize result
	res = 1

	# Find all factors that are present
	# in two or more array elements.
	x = 2 # Current factor.
	while (x <= max_num):
		
		# To store indexes of all array
		# elements that are divisible by x.
		indexes = []
		for j in range(n):
			if (arr[j] % x == 0):
				indexes.append(j)

		# If there are 2 or more array
		# elements that are divisible by x.
		if (len(indexes) >= 2):
			
			# Reduce all array elements
			# divisible by x.
			for j in range(len(indexes)):
				arr[indexes[j]] = int(arr[indexes[j]] / x)

			res = res * x
		else:
			x += 1

	# Then multiply all reduced
	for i in range(n):
		res = res * arr[i]

	return res


arr = [1, 2, 3, 4, 5, 10, 20, 35]
n = len(arr)
print(LCM(arr, n))


