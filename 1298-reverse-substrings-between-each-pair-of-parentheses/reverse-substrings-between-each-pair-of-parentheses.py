class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        s = list(s)
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(i)
            elif(s[i]==")"):
                top = stack.pop()
                a = top+1
                b = i-1
                while(a<=b):
                    s[a], s[b] = s[b], s[a]
                    a+=1
                    b-=1
        ans = ""
        for i in s:
            if i!="(" and i!=")":
                ans+=i
        return ans
                


        