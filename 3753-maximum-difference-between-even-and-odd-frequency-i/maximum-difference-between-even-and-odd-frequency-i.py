class Solution:
    def maxDifference(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        min_odd, max_odd, min_even, max_even = 150,0,150,0
        for i in d:
            if d[i]%2==0:
                if d[i] > max_even:
                    max_even = d[i]
                if d[i] < min_even:
                    min_even = d[i]
            else:
                if d[i] > max_odd:
                    max_odd = d[i]
                if d[i] < min_odd:
                    min_odd = d[i]
        return max_odd-min_even