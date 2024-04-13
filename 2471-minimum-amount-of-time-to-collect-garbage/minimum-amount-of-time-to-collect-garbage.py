class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        lastOccurences = {'M':-1, 'P':-1, 'G':-1}
        types = ['M', 'P', 'G']
        ps = [0]*len(garbage)
        for i in range(1, len(garbage)):
            ps[i] = ps[i-1] + travel[i-1]
        print(ps)
        for type in types:
            last = -1
            count = 0
            idx = 0
            for i in garbage:
                for j in i:
                    if j == type:
                        count+=1
                        last = idx
                idx+=1
            lastOccurences[type] = last
            ans+=count
            if lastOccurences[type] >= 0:
                ans+=ps[lastOccurences[type]]
        return ans
