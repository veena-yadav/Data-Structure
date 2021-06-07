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


newstack = create_stack()
push(newstack, str(6))
push(newstack, str(9))
push(newstack, str(10))
pop(newstack)
print(newstack)
