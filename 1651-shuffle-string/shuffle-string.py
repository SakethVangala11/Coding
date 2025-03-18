class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        for i in range(len(indices)):
            d[indices[i]] = s[i]
        res = ""
        for i in sorted(d.keys()):
            res+=d[i]
        return res
        