class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def push(self, x: int) -> None:
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self) -> int:
        if self.q1:
            while self.q1:
                val = self.q1.pop(0)
                if self.q1:
                    self.q2.append(val)
            return val
        else:
            while self.q2:
                val = self.q2.pop(0)
                if self.q2:
                    self.q1.append(val)
            return val
        
    def top(self) -> int:
        if self.q1:
            while self.q1:
                val = self.q1.pop(0)
                self.q2.append(val)
            return val
        else:
            while self.q2:
                val = self.q2.pop(0)
                self.q1.append(val)
            return val

    def empty(self) -> bool:
        if not self.q1 and not self.q2:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()