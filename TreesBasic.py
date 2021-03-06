class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
 
# left root right    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

# left right root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

# root left right
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)
        
# Function to print level order traversal of tree
def printLevelOrder(root):
	h = height(root)
	for i in range(1, h+1):
		printGivenLevel(root, i)


# Print nodes at a given level
def printGivenLevel(root , level):
	if root is None:
		return
	if level == 1:
		print(root.value,end=" ")
	elif level > 1 :
		printGivenLevel(root.left , level-1)
		printGivenLevel(root.right , level-1)     

# Hieght 0f tree
def height(node):
	if node is None:
		return 0
	else :
		# Compute the height of each subtree 
		lheight = height(node.left)
		rheight = height(node.right)

		#Use the larger one
		if lheight > rheight :
			return lheight+1
		else:
			return rheight+1

# def height(root):
#     if root is None:
#         return -1
    
#     leftHeight = height(root.left)
#     rightHeight = height(root.right)
    
#     return (1 + max(leftHeight, rightHeight))

# Counting no. of nodes in given tree
def countNode(root):
    if root is None:
        return 0
    return (1 + countNode(root.left) + countNode(root.right)) 

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# print("Level order traversal of binary tree is -")
# printLevelOrder(root)

# creating a tree    
    
# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(5)
# root.left.right = Node(10)
# root.right = Node(3)
# print(root.left.value)

#Traversing a tree

# preorder(root)
# postorder(root)
# inorder(root)

# print(countNode(root))
# print(height(root))


# BINARY TREES
# Max Node = 2^(h+1)
# prfect binary tree is when its all internal node have degree 2 and leaf node at same level
# Compelete binary tree is when every level must be completely filled and leaf node is at left(max)
# Degenarate binary tree is when every node has only one branch either left or right
# sekwed binary tree is when it root has only left node chain or right node chain

#--------------------------------------------------------------------------------------------------------------------------------
# BINARY TREES

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
       
def search(node, key):
    if node is None:
        return node
    
    if key == node.key:
        return node
    
    if key > node.key:
        return search(node.right, key)
    
    if key < node.key:
        return search(node.left, key)      
        
# root = None
# root =  insert(root, 10)   
# root =  insert(root, 20)
# root =  insert(root, 30)
# root =  insert(root, 40)
# root =  insert(root, 50)
        
# find1 = search(root, 51)
# print(find1)
 # to find inorder succesor       
def minvalueNode(node):
    current = node
    while current.left is not None:
         current = current.left
    return current     
  
def deleteNode(root, key):
    #if tree is empty
    if root is None:
        return root
    
    # find the node to be deleted
    if key < root.key:
        root.key = deleteNode(root.left, key)
        
    elif key > root.key:
        root.right = deleteNode(root.right, key)
        
    else:
        # if node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        # if node has two child
        temp = minvalueNode(root.right)
        root.key = deleteNode(root.right, temp.key)
        root.right = deleteNode(root.right, temp.key)
    return root

# checking node is deleted or not

# find1 = search(root, 50)
# print(find1)    
# root = deleteNode(root,50)
# find1 = search(root, 51)
# print(find1)    

#----------------------------------------------------------------------------------------------------------------------------------------
#AVL TREES
      
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        
class AvlTree(object):
    # get height of the tree
    def getHeight(self,root):
        if not root:
            return 0
        return root.height
    
    # get balance factor
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
        
    def insert(self, root, key):
        if not root:
            return TreeNode
        elif key <  root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
            
        root.height = 1+ max(self.getHeight(root.left), self.getHeight(root.right))     
        
        balance = self.getBalance(root)
        
        # ll rotation
        if balance > 1 and key < root.left.value:
            return self.rightRotate(root)
        
        # RR rotation
        if balance < -1 and key > root.left.value:
            return self.leftRotate(root)
        
        # LR rotation
        if balance > 1 and key > root.right.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        # RL rotation
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    
    def leftRotate(self, z):
        y = z.right
        t2 = y.left
        
        y.left = z
        z.right = t2
        
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
        
    def rightRotation(self,z):
        y = z.left
        t3 = y.right
        
        y.right = z
        z.left = t3
        
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y
        
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    
    def deleteNode(self, root, key):
        if not root:
            return root
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        
        if root is None:
            return root
        
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        
        # case 1 LL
        if balance >1 and self.getBalance(root.left) >= 0:
            return self.rightRotation(root)
        # case 2 RR
        if balance <-1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        # case 3 LR
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotation(root)
        # case RL
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotation(root)
            return self.leftRotate(root)
        
        return root
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# HEAP 
# every heap should be compelete binary tree and nodes are left as far as possible

def heapify(arr, n, i):
    large = i
    l = 2*i +1
    r = 2*i + 2
    if l<n and arr[i] < arr[l]:
        large = l
    if r < n and arr[large] < arr[r]:
        large = r
    if large != i:
        arr[i],arr[large] = arr[large], arr[i]
        heapify(arr, n, large)
        
def insert(arr, newNum):
    Size = len(arr)
    if Size == 0:
        arr.append(newNum)
    else:
        arr.append(newNum)
        for i in range((Size//2) -1, -1, -1):
            heapify(arr, Size, i)
            
def deleteNodefromHeap(arr, num):
    Size = len(arr)
    i = 0
    for i in range(0, Size):
        if num == arr[i]:
            break
    arr[i], arr[Size -1] = arr[Size-1],arr[i]
    arr.remove(Size-1)
    for i in range((Size//2) -1, -1, -1):
        heapify(arr, Size, i)         
# create max heap-> find largest element -> swap with last -> remove that item -> place it in sorted array
# time complexity o(nlogn)
def Heapsort(arr):
    n = len(arr)
    
    for i in range(n//2 -1,-1,-1):
        heapify(arr, n,i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0],arr[i]
        heapify(arr, i, 0)
arr = []
insert(arr, 5)
insert(arr, 10)
insert(arr, 15)
insert(arr, 20)
insert(arr, 25)
insert(arr, 30)

print("Max heap: " + str(arr))
# deleteNodefromHeap(arr,5)
# print("After dleteing a element:" + str(arr))
# arr1 = [5,50,20,10,7,15]
# Heapsort(arr1)
# n= len(arr1)
# for i in range(n):
#     print("%d " %arr1[i], end=' ')
    
#--------------------------------------------------------------------------------------------------------------------------
# priority Queue

import heapq

q= []
heapq.heappush(q,(2, 'chinky'))
heapq.heappush(q,(0, 'pinky'))
heapq.heappush(q,(1, 'tinky'))
heapq.heappush(q,(4, 'linky'))
heapq.heappush(q,(3, 'minky'))

while q:
    next = heapq.heappop(q)
    print(next)