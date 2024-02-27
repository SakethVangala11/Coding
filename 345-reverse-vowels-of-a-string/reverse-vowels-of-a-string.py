class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ""
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                vow+=i
        i = 0
        j = len(vow)-1
        res=""
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                res+=vow[j]
                j-=1
            else:
                res+=s[i]
        return res
        