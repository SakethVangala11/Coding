class Solution:
    def operate(self, s:str) -> str:
        res = ""
        n = len(s)
        for i in range(n-1):
            res+=str((int(s[i])+int(s[i+1]))%10)
        return res

    def hasSameDigits(self, s: str) -> bool:
        while(len(s)>2):
            s = self.operate(s)
        return s[0]==s[-1]       