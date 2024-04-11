class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] > i and k > 0:
                    while(stack and stack[-1] > i and k>0):
                        stack.pop()
                        k-=1
                stack.append(i)
        while(k>0):
            stack.pop()
            k-=1
        if not stack:
            return "0"
        i = 0
        while(i<len(stack) and stack[i]=="0"):
            i+=1
        if i==len(stack):
            return "0"
        return "".join(stack[i:])


            
