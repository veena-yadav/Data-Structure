# Python program to check if given number is power of 2 or not

# Function to check if x is power of 2
def isPowerOfTwo(n):
	if (n == 0):
		return False
	while (n != 1):
			if (n % 2 != 0):
				return False
			n = n // 2
			
	return True

# Driver code
# print(isPowerOfTwo(9))
