class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        setBits = 0
        for i in s:
            if i == '1':
                setBits+=1
        unSetBits = len(s)-setBits
        ans = ''
        while(setBits-1):
            ans+='1'
            setBits-=1
        while(unSetBits):
            ans+='0'
            unSetBits-=1
        ans+='1'
        return ans


        