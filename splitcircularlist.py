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
    
    def len(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
            return count

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
    
    def splitList(self,data):
        size = len(self)
        
        if size == 0:
            return 0
        if size ==1:
            return self.head

        mid = size/2
        count = 0
        prev = None
        cur = self.head

        # first list
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        # second list
        splitList = CircularLL()
        while cur.next != self.head:
            splitList.append(cur.data)
            cur = cur.next
        splitList.append(cur.data)

        

