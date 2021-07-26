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
