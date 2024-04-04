class Solution:
    def maxDepth(self, s: str) -> int:
        size = 0
        stack = []
        maxi = size
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                size+=1 
            elif s[i] == ")":
                stack.pop()
                size-=1
            maxi = max(size, maxi)
        return maxi
        