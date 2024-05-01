class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break
        ans = ""
        k =idx
        if idx>=0:
            while(idx>=0):
                ans+=word[idx]
                idx-=1
            for i in range(k+1, len(word)):
                ans+=word[i]
            return ans
        return word


        