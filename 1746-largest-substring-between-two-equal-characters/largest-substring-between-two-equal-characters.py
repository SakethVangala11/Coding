class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        maxi = -1
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]] = [i]
        
        for i in d:
            maxi = max(maxi, d[i][-1]-d[i][0]-1)
        return maxi
        