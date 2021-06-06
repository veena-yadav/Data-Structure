# tup =(10,20,40,50)
# apending in tuple
# tup = tup+(30,50,97)
# print(tup)                  #output (10, 20, 40, 50, 30, 50, 97)

# # deleting tuple
# del tup

# # set
# times = set([1,2,3,4,5,8])
# times.add(10)
# times.discard(1)
# print(times)                    #{2, 3, 4, 5, 8, 10}

# #add two tuples
# timer = set([2,30,50,8])
# print(times | timer)                # {2, 3, 4, 5, 8, 10, 50, 30}
# print(times & timer)                #  {8, 2}
# print(times <= timer)               #False

# # Dictionary

# ok = dict([(1,2),(2,3)])
# print(ok)                           #{1: 2, 2: 3}
# print(ok[2])                        # 3        (if you passed the key it will return the value)

# # change value in a dictionary
# book ={1:'intro',2:'blogs',3:'content',4:'end'}
# book[2] = 'new blogs'
# print(book)                                             #{1: 'intro', 2: 'new blogs', 3: 'content', 4: 'end'}

# # adding a new key value
# book[5] = 'review'
# print(book)                                               # {1: 'intro', 2: 'new blogs', 3: 'content', 4: 'end', 5: 'review'}

# book.clear()                                   # it will return empty dic
# book.keys()
# book.values()

# # 2-D arrary 
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(arr[1])


# #takin input and print as arrary

# size = int(input())
# array = []

# for x in range(size):
#     array.append([int(y) for y in input().split()])


# # input
# # 3
# # 10 20 30
# # 40 50 60
# # 80 20
# # #output
# # [[10, 20, 30], [40, 50, 60], [80, 20]]

# # changing the element 1
# array[0] = [1, 2]
# print(array)                                 #[[1, 2], [40, 50, 60], [80, 20]]

# print in arrary format
# arr= [[10, 20, 30], [40, 50, 60], [80, 20]]

# for x in arr:
#     for y in x:
#         print(y, end=" ")
#     print()

# output
# 10 20 30
# 40 50 60
# 80 20

# class hello:
#     def say(self):
#         print('hello')

# obj = hello()
# obj.say()                   # hello


# class hello:
#     def __init__(self,name):
#         self.name = name
    
#     def say(self,name):
#         print('hello' ,name)

# obj = hello('veena')
# print(obj.name)
# obj.say('veena') 

# output
# veena
# hello veena

class hello:
    
    def say(self,name):
        print('hello' ,name)

obj = hello()
obj.say('veena')                        # hello veena
