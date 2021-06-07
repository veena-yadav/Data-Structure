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

Q = Queue()
Q.enqueue(5)
Q.enqueue(10)
Q.enqueue(15)
Q.display()
Q.dequeue()
Q.display()

# output
# [5, 10, 15]
# [10, 15]