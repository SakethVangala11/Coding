class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        travel.insert(0,0)
        types = ['M','P','G']
        for type in types:
            a = 0
            curTravel = 0
            for i in garbage:
                count=0
                for j in i:
                    if j == type:
                        count+=1
                curTravel+=travel[a]
                a+=1
                if count:
                    ans+=count
                    ans+=curTravel
                    curTravel = 0
        return ans      