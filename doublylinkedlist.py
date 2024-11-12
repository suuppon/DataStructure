class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node() #Dummy Node
        self.size = 0
        
    def splice(self, a, b, x):
        '''
        조건 1 : a의 next를 따라가다 보면 b가 나온다.
        조건 2 : a와 b 사이에 head가 존재하지 않는다.
        '''
        ap = a.prev
        bn = b.next
        xn = x.next
        
        # Cut
        ap.next = bn
        bn.prev = ap
        
        xn.next = a
        a.prev = x
        b.next = xn
        xn.prev = b
        
    def moveAfter(self, a, x):
        self.splice(a, a, x)
        
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)
        
    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)
        
    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)
        
    def pushFront(self, key):
        self.insertAfter(self.head, key)
    
    def pushBack(self, key):
        self.insertBefore(self.head, key)
        
    def search(self, key):
        v = self.head.next # Dummy Node
        while v.key != None:
            if v.key == key:
                return v
            v = v.next
        return None
    
    def remove(self, x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        del x
        
    def popFront(self):
        x = self.head.next
        self.remove(x)
        return x
    
    def popBack(self):
        x = self.head
        
        while x.next != None:
            x = x.next
        self.remove(x)
        return x