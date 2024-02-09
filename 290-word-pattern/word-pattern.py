class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=list(map(str,s.split()))
        d={}
        se=set()
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]]!=s[i]:
                    return False
            else:
                d[pattern[i]]=s[i]
                if s[i] in se:
                    return False
                se.add(s[i])
        return True
        
        