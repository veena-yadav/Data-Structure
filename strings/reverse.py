#Write a function that reverses a string. The input string is given as an array of characters s.
def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        while left<=right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s
    
# s = ["h","e","l","l","o"]
# print(reverseString(s))

#33333333333333333333333333333333333333333333333333333333333333333333
def reverse(x):
    if x==0:
        return 0
    str_n = str(abs(x))[::-1]
    if int(str_n)<2**31:
        if x >0 :
            return int(str_n)
        return -int(str_n)
    return 0

# x = -123
# print(reverse(x))

#################################################################
from collections import Counter
def firstUniqChar(s):
	# Dictionary to maintain count
    count = {}
	# Iterate through each character and update the count
    for c in s:
        keys = count.keys()
        if(c in keys):
            count[c]+=1
        else:
            count[c]=1
	# Return the index, if count is 1
    for i in range(len(s)):
        if(count[s[i]]==1):
            return i
    return -1
    
    # count = collections.Counter(s)
        
    #     # find the index
    # for idx, ch in enumerate(s):
    #     if count[ch] == 1:
    #         return idx     
    # return -1
s = "loveleetcode"
print(firstUniqChar(s))
