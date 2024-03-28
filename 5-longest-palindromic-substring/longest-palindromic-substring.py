class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        res = ""

        for i in range(len(s)):

            #Odd length Palindromic substring

            a, b = i, i
            while(a>=0 and b<len(s)):
                if s[a]==s[b]:
                    a-=1
                    b+=1
                else:
                    break 
            if b-a-1 > maxlen:
                maxlen = b-a-1
                res = s[a+1:b]

            #Even length Palindromic substring

            a, b = i, i+1
            while(a>=0 and b<len(s)):
                if s[a]==s[b]:
                    a-=1
                    b+=1
                else:
                    break 
            if b-a-1 > maxlen:
                maxlen = b-a-1
                res = s[a+1:b]
        return res


        


                
        