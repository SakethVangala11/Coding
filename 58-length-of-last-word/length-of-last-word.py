class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        count = 0
        flag = 0
        while(i>=0):
            while(s[i]==" " and flag==0):
                i-=1
            flag = 1
            if s[i] == " ":
                break
            else:
                count+=1
            i-=1
        return count
            
            

        