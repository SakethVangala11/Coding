class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and (abs(ord(stack[-1]) - ord(s[i]))) == 32:
                stack.pop()
                continue
            stack.append(s[i])
        return "".join(stack)
            




        
        





        