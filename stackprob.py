n = int(input())
stack =[]

for i in range(n):
    num = input()
    query = num[0]
    # on 0 it will pushed element
    if query == '0':
        val = int(num[2:])
        if len(stack) ==0:
            stack.append(val)
        else:
            currMax = stack[-1]
            stack.append(val if val>currMax else currMax)
    # on 1 it will pop the element
    elif query== '2':
        stack.pop()
    # else it will return max element
    else:
        print(stack[-1])