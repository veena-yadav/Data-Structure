def search(pat,text):
    n= len(text)
    m = len(pat)
    
    for i in range(n-m+1):
        j = 0
        while j<m :
            if text[i+j] != pat[j]:
                break
            j += 1
            
        if j == m:
            print("index: ",i)
            
            
# txt = "AABAACAADAABAAABAA"
# pat = "AABA"
# search(pat, txt)

###########################################################
# Python does not have a character data type, a single character is simply a string with a length of 1.
 
# txt = "The best things in life are free!"
# print("free" in txt)

# a = "Hello, World!"
# print(a.replace("H", "J"))

# some functions len,upper,lower, strip

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# The escape character allows you to use double quotes when you normally would not be allowed:
# txt = "We are the so-called \"Vikings\" from the north."

# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)

# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

# Make the first letter in each word upper case:
# txt = "Welcome to my world"
# x = txt.title()

##########################################################
"""Input:
str = 101
Output:
1
Explanation:
Since string contains only 0 and 1, output is 1.

Input:
str = 75
Output:
"""
def isBinary(str):
    
    x = set(str)
    p = {"0","1"}
    
    if p == x or x == {'0'} or x == {'1'}:
        return 1
    else :
        return 0

################################################

def convertRoman(n):
    #Code here
    val = [1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1 ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"]
    roman_num = ''
    i = 0
    while  n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num

"""Input:
n = 3
Output: III"""

#####################################################
def getMaxOccurringChar(str):
        ASCII_SIZE = 256
    
        count = [0] * ASCII_SIZE
     
        # Utility variables
        max = -1
        c = ''
        
        for i in str:
            count[ord(i)] +=1
     
        for i in str:
            if max < count[ord(i)]:
                max = count[ord(i)]
                c = i
     
        return c
    
# Driver program to test the above function
str = "output"
# print ("Max occurring character is " + getMaxOccurringChar(str))

##################################################################
def missingPanagram(self, Str):
    MAX_CHAR = 26
    present = [False for i in range(MAX_CHAR)]
 
    for i in range(len(Str)):
        if (Str[i] >= 'a' and Str[i] <= 'z'):
            present[ord(Str[i]) - ord('a')] = True
        elif (Str[i] >= 'A' and Str[i] <= 'Z'):
            present[ord(Str[i]) - ord('A')] = True
     
    res = ""
     
    for i in range(MAX_CHAR):
        if (present[i] == False):
            res += chr(i + ord('a'))
                 
    if len(res) != 0:
        return res
    return -1

"""
Input:
s = Abcdefghijklmnopqrstuvwxy
Output: z"""

###################################################

#Function to locate the occurrence of the string x in the string s.
def strstr(s,x):

    if x in s:
        return s.find(x)
    return -1

# s = GeeksForGeeks, x = Fr
# Output: -1

# s = GeeksForGeeks, x = For
# Output: 5
#####################################################33

def areRotations(s1,s2):
    temp = '' 
      
    if len(s1) != len(s2): 
        return False
   
    temp = s1 + s1 
        
    if s2 in temp: 
        return True #returning true if 2nd string is present in concatenated string
    else: 
        return False
    
string1 = "geeksforgeeks"
string2 = "forgeeksgeeks"
  
# if areRotations(string1, string2): 
#     print("Given Strings are rotations of each other.")
# else: 
#     print("Given Strings are not rotations of each other.")

####################################################
def isAnagram(a,b):
    n1 = len(a)
    n2 = len(b)
    if n1 != n2:
        return("NO")
    s1 = sorted(a)
    s2 = sorted(b)
        
    for i in range(0,n1):
        if s1[i] != s2[i]:
            return("NO")
    return("Yes")

str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
 
# print(isAnagram(str1,str2))
def isValid(s):

    l= s.split(".")
    for x in l:
        if len(x) == 0 or len(x) > 3:
            return 0
          
        if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
            return 0
    return 1
    # for i in range(len(l)):
    #     if i <=0 and i>=255:
    #         return 0
    # return 1

s = "125.220.100.1"
# print(isValid(s))