class Solution:
    def result(self,pattern):
        l = []
        for i in pattern:
            if i == '#':
                if l:
                    l.pop()
            else:
                l.append(i)
        return l

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.result(s) == self.result(t)
        
        
        