class Solution:
    def findValidPair(self, s: str) -> str:
        d = {}
        n=len(s)
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in range(n-1):
            if s[i]!=s[i+1] and d[s[i]]==int(s[i]) and d[s[i+1]]==int(s[i+1]):
                return s[i]+s[i+1]
        return ""

        