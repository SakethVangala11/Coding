class Solution:
    def countPoints(self, rings: str) -> int:
        a = [set() for i in range(10)]
        for i in range(len(rings)):
            if i%2==0:
                col = rings[i]
                pos = rings[i+1]
                a[int(pos)].add(col)
            else:
                pass
        count = 0
        for i in a:
            if len(i)==3:
                count+=1
        return count

        