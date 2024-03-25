class MyHashMap:

    def __init__(self):
        self.l = [float('inf')]*1000001

    def put(self, key: int, value: int) -> None:
        self.l[key] = value
        
    def get(self, key: int) -> int:
        if self.l[key]==float('inf'):
            return -1
        return self.l[key]
        
    def remove(self, key: int) -> None:
        self.l[key] = float('inf')
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)