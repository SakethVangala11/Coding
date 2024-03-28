class Node:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [Node() for i in range(1000)]
        
    def put(self, key: int, value: int) -> None:
        mod = key%1000
        head = self.map[mod]
        cur = head
        prev = None
        while(cur):
            if cur.key == key:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
        node = Node(key, value)
        while(prev.next):
            prev = prev.next
        prev.next = node
        
    def get(self, key: int) -> int:
        mod = key%1000
        head = self.map[mod]
        cur = head
        while(cur):
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        mod = key%1000
        head = self.map[mod]
        prev = None
        cur = head
        while(cur):
            if cur.key == key:
                prev.next = cur.next
            prev = cur
            cur = cur.next
    
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)