#Create a Node class to create node for doubly linkedlist
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    #Init capacity and cache to store key and values as pointer to nodes. 
    #Create left and right pointers as dummy nodes and connect them init.
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    #To remove a node that is passed. So we can take prev node and next node based on current node
    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    #Inserting a node always happens at the end as right pointer has MRU
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        node.prev = prev
        prev.next = node
        node.next = nxt
        nxt.prev = node

    #If key is present remove from linkedlist and insert at the end and return it's value
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    #While insertion, if key is already in hashmap, we have to remove it and create a new node and add to end.
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        # After adding if len is more than capacity, remove lru that is next to left pointer then del from hashmap.
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)