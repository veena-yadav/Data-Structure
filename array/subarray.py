#sub array n*(n+1)/2
def subarray(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i:j+1])
            
arr = [1,2,3,4,5]
# subarray(arr)

#substrings n*(n+1)/2

def substring(str):
    for i in range(len(str)):
        for j in range(i, len(str)):
            print(str[i:j+1], end = ' ')
            
str = 'python'
substring(str)

# sub= sequence 2^n
def subsequence(str, substr= ''):
    if len(str) == 0:
        print(substr, end = ' ')
        return
    subsequence(str[:-1], substr + str[-1])
    subsequence(str[:-1], substr)
    return
    
    
str = "abc"
# subsequence(str)

# python3 program for power set 

import math; 

def printPowerSet(set,set_size): 
	
	# set_size of power set of a set 
	# with set_size n is (2**n -1) 
	pow_set_size = (int) (math.pow(2, set_size)); 
	counter = 0; 
	j = 0; 
	
	# Run from counter 000..0 to 111..1 
	for counter in range(0, pow_set_size): 
		for j in range(0, set_size): 
			
			# Check if jth bit in the 
			# counter is set If set then 
			# print jth element from set 
			if((counter & (1 << j)) > 0): 
				print(set[j], end = ""); 
		print(""); 

# Driver program to test printPowerSet 
# set = ['a', 'b', 'c']; 
# printPowerSet(set, 3); 
