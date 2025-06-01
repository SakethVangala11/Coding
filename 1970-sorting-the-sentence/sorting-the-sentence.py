class Solution:
    def sortSentence(self, s: str) -> str:
        words = list(map(str, s.split(' ')))
        d = {}
        for i in words:
            d[int(i[-1])]=i[0:-1]
        ans = ""
        for i in range(len(words)):
            ans+=d[i+1]
            if(i < len(words)-1):
                ans+=" "
        return ans
        