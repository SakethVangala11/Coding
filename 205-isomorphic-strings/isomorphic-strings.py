class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        n = len(s)
        m = len(t)
        se = set()
        if n!=m:
            return False
        for i in range(m):
            x = s[i]
            y = t[i]
            if x in d:
                if d[x]!=y:
                    return False
            else:
                if y not in se:
                    d[x] = y 
                    se.add(y)
                else:
                    return False
        return True
        