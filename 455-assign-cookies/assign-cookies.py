class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort(reverse = True)
        s.sort()
        j = len(g)-1
        for i in range(len(s)):
            if j>=0 and s[i] >= g[j]:
                j-=1
                count+=1
            else:
                pass
        return count




        
        