class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substr = []
        for i in range(len(s)):
            temp = ""
            for j in range(i,len(s)):
                temp+=s[j]
                se = set(temp)
                if j-i+1 >=minSize and j-i+1 <=maxSize and len(se)<=maxLetters:
                    substr.append(temp)
                if j-i+1>maxSize or len(se)>maxLetters:
                    break
        d = {}
        for i in substr:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        if d:
            return max(list(d.values()))
        return 0
        