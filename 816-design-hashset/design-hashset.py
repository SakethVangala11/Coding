class Node:
    def __init__(self, key = -1, next = None):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.hashSet = [Node(-1) for i in range(10000)]
        

    def add(self, key: int) -> None:
        mod = key%10000
        head = self.hashSet[mod]
        cur = head
        while(cur.next):
            if cur.key == key:
                break
            cur = cur.next
        if cur.key!= key:
            cur.next = Node(key)
        
    def remove(self, key: int) -> None:
        mod = key%10000
        head = self.hashSet[mod]
        cur = head
        prev = None
        while(cur):
            if cur.key == key:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
        
    def contains(self, key: int) -> bool:
        mod = key%10000
        head = self.hashSet[mod]
        cur = head
        while(cur):
            if cur.key == key:
                return True
            cur = cur.next
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)