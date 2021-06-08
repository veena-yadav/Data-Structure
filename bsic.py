# stack

# def create_stack():
#     stack = []
#     return stack

# def check_empty(stack):
#     return len(stack)==0

# def push(stack, item):
#     stack.append(item)
#     print('pushed item '+ item)

# def pop(stack):
#     if(check_empty(stack)):
#         return "stack is empty"
#     else:
#         item = stack.pop()
#         print('poped element: ', item)


# newstack = create_stack()
# push(newstack, str(6))
# push(newstack, str(9))
# push(newstack, str(10))
# print(newstack)
# pop(newstack)
# print(newstack)


#--------------------------------------------------------------------------------------------------------------------------------------
#Queue

# class Queue:
#     def __init__(self):
#         self.queue = []
         
#     def enqueue(self, item):
#         self.queue.append(item)

#     def dequeue(self):
#         if(len(self.queue)<1):
#             return None
#         return self.queue.pop(0)

#     def display(self):
#         print(self.queue)

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
#---------------------------------------------------------------------------------------------------------------------------------------------------

# linked list

class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next


class LL:
    def __init__(self):
        self.head = head

# printing a data
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

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
        

linkedlist = LL()
linkedlist.pushBeg(5)
linkedlist.pushBeg(10)
linkedlist.pushAfter(1, 15)
linkedlist.pushLast(20)
linkedlist.printList()
linkedlist.DeleteAfter(1)











