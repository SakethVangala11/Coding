class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1

        count = 0
        flag = 0
        for i in d:
            if d[i]%2==0:
                count+=d[i]
            else:
                flag = 1
                count+=d[i]-1
        if flag:
            return count+1
        else:
            return count





        