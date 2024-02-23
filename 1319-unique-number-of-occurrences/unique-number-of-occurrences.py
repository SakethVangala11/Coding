class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l = list(d.values())
        n = len(l)
        l =set(l)
        if n == len(l):
            return True
        return False

        if len(d) == len(set(d.values())):
            return True
        else:
            return False