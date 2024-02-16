class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        n_d = len(d)
        sorted_d = dict(sorted(d.items(), key = lambda x:x[1]))
        count=0
        for i in sorted_d:
            if k >=d[i]:
                k-=d[i]
                count+=1
        return n_d-count

