class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        
    def __str__(self):
        '''
        Print 함수 호출 시 key값을 string으로 리턴
        '''
        return str(self.key)
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pushBack(self, key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node
        self.size += 1
        
    def popFront(self):
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key
            '''
            Delete x
            '''
            self.head = x.next
            self.size -= 1
            return key
        
    def popBack(self):
        if len(self) == 0:
            return None
        else:
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            
            if len(self) == 1:
                self.head = None
            else:
                '''
                Delete tail
                '''
                prev.next = None
            self.size -= 1
            return tail.key
        
    def search(self, key):
        value = self.head
        
        if len(self) == 0:
            return None
        else:
            while value != None:
                if value.key == key:
                    return value
                value = value.next
        
        return None
    
    def __iterator__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next    