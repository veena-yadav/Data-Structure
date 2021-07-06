def CalDigitsInNum(x):
    count = 0
    if x == 0:
        count = 1
    else:
        while x != 0:
            x = x//10
            # print(x)
            count += 1 
    return count

print(CalDigitsInNum(345289467))

# function to import ceil and log
import math
 
def countDigit(n):
    return math.floor(math.log10(n)+1)

print(countDigit(345289467))

def isPrime(N):
    if N > 1:
        for i in range(2, int(N/2)+1):
            if (N % i) == 0:
                return("No")
                break
            else:
                return("Yes")
 
        else:
            return("No")
        
print(isPrime(32))