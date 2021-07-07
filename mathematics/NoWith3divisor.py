# program to print all three-primes smaller than or equal to n without using extra space

# 3 divisor logic implementation check if a number is prime or not if it is a prime then check
# if its square is less than or equal to the given number
def numbersWith3Divisors(n):

	print("Numbers with 3 divisors : ")
	
	i = 2
	while i * i <= n:
		if (isPrime(i)):
			if (i * i <= n):
				print(i * i, end = " ")	
		i += 1

def isPrime(n):
	if (n == 0 or n == 1):
		return False

	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
			
		i += 1

	return True

n = 9

numbersWith3Divisors(n)

