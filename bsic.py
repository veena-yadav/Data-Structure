# stack

def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)
    print('pushed item '+ item)

def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"
    else:
        item = stack.pop()
        print('poped element: ', item)


# 


# --------------------------------------------------------------------------------------------------------------------------------------
# Queue

class Queue:
    def __init__(self):
        self.queue = []
         
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if(len(self.queue)<1):
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

# Q = Queue()
# Q.enqueue(5)
# Q.enqueue(10)
# Q.enqueue(15)

# Q.display()
# Q.dequeue()
# Q.display()

# output
# [5, 10, 15]
# [10, 15]
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# linked list

class Node:
    def __init__(self,data, next):
        self.data = data
        self.next = next

class LL:
    def __init__(self):
        self.head = None

# printing a data
    def printList(self):
        cur = self.head
        while(cur):
            print(cur.data)
            cur = cur.next

# push a element in front
    def pushBeg(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

# push a element at given point
    def pushAfter(self, prevNode ,newData):
    
        if prevNode is None:
            print('list is empty')
        
        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode

# push a element at end point
    def pushLast(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return
        
        last = self.head
        while (last.next):
            last = last.next
            last.next = newNode

# Deleting a node

    def DeleteAfter(self, pos):
        curNode = self.head
        prev = None
        count = 0

        while curNode and count != pos:
            prev = curNode
            curNode = curNode.next
            count += 1

        if curNode is None:
            return

        prev.next = curNode.next
        curNode = None
        

# linkedlist = LL()
# linkedlist.pushBeg(5)
 
# linkedlist.pushBeg(10)
# # linkedlist.pushAfter(1,15)
# linkedlist.pushLast(20)
# linkedlist.printList()
# linkedlist.DeleteAfter(1)

# ------------------------------------------------------------------------------------------------------------------------------------------------
# doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoubltLinkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append(self,data):
        if self.head is None:
            newNode = Node(data)
            newNode.prev = None
            self.head = newNode
        else:
            newNode = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next= newNode
            newNode.prev = cur
            newNode.next = None

    def prepand(self,data):
        if self.head is None:
            newNode = Node(data)
            newNode.prev = None
            self.head = newNode

        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None

    def delete(self,key):
        cur = self.head

        while cur:
            if cur.data== key and cur ==self.head:
                #if only one node is there
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # to delete first node
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif cur.data == key:
                # To delete middle element
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt

                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

#------------------------------------------------------------------------------------------------------------------------------------------------

#circular linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = next


class CircularLL:
    def __init__(self):
        self.head = None

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head

        else:
            newNode = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head

    def prepond(self,data):
        newNode = Node(data)
        cur = self.head
        newNode.next = self.head

        if not self.head:
            newNode.next = newNode 

        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
        
        self.head = newNode
    
    def DeleteLast( self, head):
        current = head
        temp = head
        previous = None

        if (head == None):
            print("\nList is empty")
            return None

        if (current.next == current):
            head = None
            return None

        while (current.next != head):
            previous = current
            current = current.next

        previous.next = current.next
        head = previous.next

        return head

#-------------------------------------------------------------------------------------------------------------------------------

# Double Ended Queue

class deque:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addRear(self,item):
        self.items.append(item)
        
    def addFront(self, item):
        self.items.insert(0, item)
        
    def removefront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
# d= deque()
# d.addFront(5)
# d.addRear(10)
# d.addRear(15)
# print(d.size())

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
from typing import Tuple


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """
    
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1
    

def add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                child.counter += 1
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return 
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True, node.counter

if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "hackathon")
    add(root, 'hack')

    print(find_prefix(root, 'hac'))
    print(find_prefix(root, 'hack'))
    print(find_prefix(root, 'hackathon'))
    print(find_prefix(root, 'ha'))
    print(find_prefix(root, 'hammer'))






















