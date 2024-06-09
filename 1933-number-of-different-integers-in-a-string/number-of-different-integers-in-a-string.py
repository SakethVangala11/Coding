class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ""
        for i in word:
            if ord(i)>96 and ord(i)<123:
                s+=" "
            else:
                s+=i
        l = s.split(" ")
        se = set()
        for i in l:
            if i:
                se.add(int(i))
        return len(se)
        