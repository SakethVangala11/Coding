class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        x, y = '', ''
        for i in range(n):
            if i%2==0:
                x+='1'
                y+='0'
            else:
                x+='0'
                y+='1'
        c1, c2 =0, 0
        for i in range(n):
            if s[i]!=x[i]:
                c1+=1
            if s[i]!=y[i]:
                c2+=1
        return min(c1, c2)
        