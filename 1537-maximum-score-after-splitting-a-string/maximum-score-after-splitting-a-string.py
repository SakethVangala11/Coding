class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        psz = [0]*n
        pso = [0]*n
        count = 0
        for i in range(n):
            if s[i] == '0':
                count+=1
            psz[i] = count

        count = 0
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                count+=1
            pso[i] = count

        maxi = 0
        for i in range(n-1):
            cur  = psz[i] + pso[i+1]
            maxi = max(maxi, cur)
        return maxi

        