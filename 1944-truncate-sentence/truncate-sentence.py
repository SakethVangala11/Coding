class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = ""
        spaces = 0
        i=0
        while(spaces < k and i<len(s)):
            if(s[i]==" "):
                spaces+=1
            if spaces==k:
                break
            ans+=s[i]
            i+=1
        return ans 
        