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
# class HashTable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [[] for i in range(self.MAX)]
        
#     def get_hash(self,key):
#         hash = 0
#         for every_char in key:
#             hash += ord(every_char)
#         return hash % 100
    
#     # set items
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         found = False 
#         for idx, element in enumerate(self.arr[h]):
#             #colision handling
#             if len(element) == 2 and element[0] == key:
#                 self.arr[h][idx] = (key,val)
#                 found = True
#         if not found:
#             self.arr[h].append(key,val)
        
#     # delete item
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         self.arr[h]= None
        
#     # get item
#     def __getitem__(self,key):
#         arr_index = self.get_hash(key)
#         for kv in self.arr[arr_index]:
#             if kv[0] == key:
#                 return
            
    
# GRAPH

class Graph(object):
    
    def __init__(self, size):
        self.adjmatrix = []
        self.size = size
        for i in range(size):
            self.adjmatrix.append([0 for i in range(size)])
            
    def AddEdge(self,v1,v2):
        if v1 ==v2:
            print("same vertex %d and %d" %(v1,v2))
        self.adjmatrix[v1][v2] = 1
        
    def removeEdge(self,v1,v2):
        if self.adjmatrix[v1][v2] == 0:
            print("No edge between %d and %d" %(v1,v2))
            return
        self.adjmatrix[v1][v2] = 0
            
    def __len__(self):
        return self.size
    
    def printMatrix(self):
        for row in self.adjmatrix:
            for val in row:
                print('{:4}'.format(val), end = '')
            print()
import collections

def bfs(Graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    
    while queue:
        #deque a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + ' ', end='')
        
        #if not visited marked it as visited, and enqueue it
        for neighbor in Graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
def dfs(graph,start, visited= None):
    if visited is None:
        visited = set()
        
    visited.add(start)
    print(start)
    
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
# def main():
    # g = Graph(5)
    # g.AddEdge(0,1)
    # g.AddEdge(0,2)
    # g.AddEdge(1,2)
    # g.AddEdge(2,0)
    # g.AddEdge(2,3)
    # g.printMatrix()
    # print('removing edge')
    # g.removeEdge(2,3)
    # g.printMatrix()
    
if __name__ == '__main__':
    # main()
    g = {0:[1,2], 1:[2], 2:[3], 3:[1,2]}
    bfs(g,0)
    print()
    print("dfs")
    g2 = {'0': set(['1','2']),
          '1': set(['0','3','4']),
          '2': set(['0']),
          '3': set(['1']),
          '4': set(['2','3'])}
    
    dfs(g2,'0')

# connected graph each vertex have path to reach there with another vertex. all other

# prism algorithm

INF = 99999999
V = 5
G = [[0,9,75,0,0],
     [9,0,95,19,42],
     [75,95,0,51,66],
     [0,19,51,0,91],
     [0,42,66,31,0]]

selected = [0,0,0,0,0]
no_edge = 0

selected[0] = True
print('Edge : Weight\n')
while(no_edge < V-1):
    min = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j] and G[i][j]):
                    if min > G[i][j]:
                        min = G[i][j]
                        x = i
                        y = j
    print(str(x) + '-' + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1
    

# Kruskal's algorithm in Python


class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()


