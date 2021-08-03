class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to reverse the linked list
	def reverse(self):
		prev = None
		current = self.head
		while(current):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev
  
    
	# Function to insert a new node at the beginning
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data,end=" ")
			temp = temp.next
# method one of detect loop
    # def detectLoop(self):
    #     s = set()
    #     cur = self.head
    #     while(cur):
    #         if cur in s:
    #             return True
    #         s.add(cur)
    #         cur = cur.next
    #         return False
    # method 2
    
    # def detectloop(self):
    #     slow = self.head
    #     fast = self.head
    #     while(slow and fast and fast.next):
    #         slow = slow.next
    #         fast = fast.next.next
    #         if slow == fast:
    #             return("loop is present")
    #         return("no loop")
    
# def intersectionNode(firstList,SecondList):
#     s= set()

#     while firstList:
#         s.add(firstList)
#         firstList =  firstList.next
        
#     while SecondList:
#         if SecondList in s:
#             return SecondList
#         SecondList = SecondList.next

#     return "no instection element"      

# pairwise swapping of node
    # def pairWiseSwap(self, head):
        
    #     temp = head
    #     if temp is None:
    #         return
        
    #     while temp and temp.next:
    #         if temp.data != temp.next.data:
    #             temp.data, temp.next.data = temp.next.data, temp.data
                
    #         temp = temp.next.next
            
    #     return temp  
    



llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print ("Given Linked List")
# print(detectloop())
llist.printList()
# llist.reverse()
# print ("\nReversed Linked List")
# llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)



        