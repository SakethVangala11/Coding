class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in s:
            if ord(i) > 96 and ord(i)<123:
                stack.append(i)
            else:
                stack.pop()
        ans = ""
        for i in stack:
            ans+=i
        return ans

        