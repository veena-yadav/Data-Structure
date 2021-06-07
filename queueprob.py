# queue using two stack

front = []
back = []

def pushBack():
    if back:
        return 
    while front:
        item = front.pop(-1)
        back.append(item)

def dequeue():
    pushBack()
    back.pop()

def enqueque(x):
    front.append(x)

q = int(input())

for i in range(q):
    split = list(map(int, input().split()))

    if (split[0] ==1):
        enqueque(split[1])
    elif (split[0] ==2):
        dequeue()
    else:
        pushBack()
        print(back[-1])