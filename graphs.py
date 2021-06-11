# HASHMAP

# class HashTable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]
        
#     def get_hash(self,key):
#         hash = 0
#         for every_char in key:
#             hash += ord(every_char)
#         return hash % 100
    
#     # set items
#     def __setitem__(self,key,val):
#         h = self.get_hash(key)
#         self.arr[h] = val
        
#     # delete item
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         self.arr[h]= None
        
#     # get item
#     def __getitem__(self,index):
#         h = self.get_hash(index)
#         return self.arr[h]

# t = HashTable()
# t["march 6"] = 310
# t["march 7"] = 420
# print(t["march 7"])

# if hash function giving same value for two differnt data elements then it is called collision
# chaining and linear probing can handle the collision
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self,key):
        hash = 0
        for every_char in key:
            hash += ord(every_char)
        return hash % 100
    
    # set items
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False 
        for idx, element in enumerate(self.arr[h]):
            #colision handling
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append(key,val)
        
    # delete item
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h]= None
        
    # get item
    def __getitem__(self,key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return
            
    












