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
    
# spliting a circular linked list
def splitList( head, head1, head2):
        #code here
        fast = head
        slow = head
        while fast.next != head and fast.next.next != head :
            fast = fast.next.next
            slow = slow.next
            
            if fast.next.next == head:
                fast = fast.next
            head1.head = head
     
            if head.next != head:
                head2.head = slow.next
     
            fast.next = slow.next
         
            slow.next = head
        
        
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2

# delete middle node of a linked list.
def countOfNodes(head):
        count =0
        cur = head
        while cur:
            cur = cur.next
            count += 1
        return count
def deleteMid(head):
    
    copyhead = head
    if head ==None:
        return None
    if head.next == None:
        del(head)
        return None
        
    totalnode = countOfNodes(head)
    mid = totalnode // 2
  
    # Delete the middle node
    while (mid > 1):
        mid -= 1
        head = head.next
  
    # Delete the middle node
    head.next = head.next.next
  
    return copyhead
    
   ####################################################################### 
#Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        node = curr_node
        prev=None
        while node.next:
            node.data=node.next.data
            prev=node
            node=node.next
        prev.next=None
########################################################################
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return 
    
        curr = head

        #creating a copy of each node in the original linkedlist using next pointer
        while curr:

            new = curr.next
            curr.next = Node(curr.val)
            curr.next.next = new
            curr  = new


            curr_rd = head

       #adding the random pointer to the newly created nodes
        while curr_rd:
            if curr_rd.random:
                curr_rd.next.random = curr_rd.random.next
            curr_rd = curr_rd.next.next


        second = cur = head.next

        #separating the copy and original linked list
        while cur.next:
            cur.next = cur.next.next        
            cur = cur.next
        head.next = None

        #return the head of cloned linkedlist
        return second

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



        