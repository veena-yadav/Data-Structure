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
# s = "loveleetcode"
# print(firstUniqChar(s))

"""b = Counter({'geeks' : 4, 'for' : 1,'gfg' : 2, 'python' : 3})
 
for i in b.elements():
    print(i, b[i])"""


#############################################################33
def isAnagram(s,t):
    s="".join(sorted(s))
    t="".join(sorted(t))
    if s==t:
        return True
    else:
        return False
#         sfreq=collections.Counter(s)
#         tfreq=collections.Counter(t)
#         s_size=len(sfreq)
#         t_size=len(tfreq)
        
#         for letter in sfreq:
#             if tfreq[letter] != sfreq[letter]:
#                 return False
            
#             t_size-=1
#             s_size-=1
#         return t_size == s_size == 0

##############################################################
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
def isPalindrome(s):
    import re
    s = re.sub('[^a-zA-Z0-9]', '', s).lower()
    p1 = 0
    p2 = len(s) - 1
    while p1 < p2:
        if s[p1] != s[p2]: return False
        p1 += 1
        p2 -= 1
    return True

# s = "A man, a plan, a canal: Panama"
# print(isPalindrome(s))

################################################################################
"""Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 we will return 0 when needle is an empty string
 
 Input: haystack = "hello", needle = "ll"
Output: 2
 """
def strStr(self, haystack: str, needle: str) -> int:
    if haystack == "" and needle == "":
        return 0
    if needle not in haystack:
        return -1
    elif needle in haystack:
        return haystack.find(needle)
    
    
######################################################################
"""Input: strs = ["flower","flow","flight"]
Output: "fl"""
def longestCommonPrefix(strs):
    prefix=""
    if len(strs)==0: return prefix

    for i in range(len(min(strs))):
        c=strs[0][i]
        if all(a[i]==c for a in strs):
            prefix+=c
        else:
            break
    return prefix
        