class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxi = -1
        for i in strs:
            flag = 0
            for j in i:
                if (ord(j)>=65 and ord(j)<91) or (ord(j)>=97 and ord(j)<123):
                    flag = 1
            if flag:
                maxi = max(maxi, len(i))
            else:
                maxi = max(maxi, int(i))
        return maxi
