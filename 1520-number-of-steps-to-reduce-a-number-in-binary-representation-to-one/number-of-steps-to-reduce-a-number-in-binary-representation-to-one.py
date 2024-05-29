class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        k = 0
        for i in range(len(s)-1, -1, -1):
            if s[i]=='1':
                num+=2**k
            k+=1
        steps = 0
        while(num!=1):
            if num%2==1:
                num+=1
                steps+=1
            else:
                num//=2
                steps+=1
        return steps


        