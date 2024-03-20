class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index: int) -> int:
        if index < 0 or index >=self.size or not self.head:
            return -1

        cur = self.head
        count = 0 
        while(count<index):
            cur = cur.next
            count+=1
        return cur.val


    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head 
        self.head = node
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        cur = self.head
        if not self.head:
            self.head = node
            self.size+=1
            return 
        while(cur.next):
            cur = cur.next
        cur.next = node
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index>self.size:
            return 
        if index == 0:
            return self.addAtHead(val)
        elif index == self.size:
            return self.addAtTail(val)

        prev = None
        cur = self.head
        count = 0
        while(count<index):
            prev = cur
            cur = cur.next
            count+=1
        node = Node(val)
        prev.next = node
        node.next = cur
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >=self.size:
            return 
        if index == 0:
            self.head = self.head.next
        else:
            count = 0
            cur = self.head
            prev = None
            while(count<index):
                prev = cur
                cur = cur.next
                count+=1
            prev.next = cur.next
        self.size-=1
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)