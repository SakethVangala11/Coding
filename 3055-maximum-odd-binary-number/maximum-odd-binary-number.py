class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        setBits = 0
        for i in s:
            if i == '1':
                setBits+=1
        unSetBits = len(s)-setBits
        return '1'*(setBits-1) + '0'*unSetBits + '1'


        