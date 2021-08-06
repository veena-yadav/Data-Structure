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
