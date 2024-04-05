class Solution:
    def largestOddNumber(self, num: str) -> str:
        b = -1
        for i in range(len(num)-1, -1, -1):
            if int(num[i])%2==1:
                b = i
                break
        if i==-1:
            return ""
        return num[0:b+1]



        

        