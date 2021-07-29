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
############################################
# Given a number N, find the most significant set bit in the given number.
"""Input : N = 10
Output : 8
Binary representation of 10 is 1010
The most significant bit corresponds
to decimal number 8.

Input : N = 18
Output : 16"""
def setBitNumber(n):
    if (n == 0):
        return 0
 
    msb = 0
    n = int(n / 2)
 
    while (n > 0):
        n = int(n / 2)
        msb += 1
 
    return (1 << msb)

print(setBitNumber(18))
