def permute(s, answer):
	if (len(s) == 0):
		print(answer, end = " ")
		return
	
	for i in range(len(s)):
		ch = s[i]
		left_substr = s[0:i]
		right_substr = s[i + 1:]
		rest = left_substr + right_substr
		permute(rest, answer + ch)

# Driver Code
# answer = ""

# s = input("Enter the string : ")

# print("All possible strings are : ")
# permute(s, answer)

#cal permutation
def npr(n, r):
    return (fact(n) / fact(n - r))

#cal combination
def nCr(n, r):
    return (fact(n) / (fact(r)
                * fact(n - r)))
 
def fact(x):
    if x==1:
        return 1
    return (fact(x-1)*x)


n = 5
r = 3
print(int(nCr(n, r)))
print(int(npr(n, r)))