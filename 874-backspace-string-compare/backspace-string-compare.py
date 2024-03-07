class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sr = ""
        tr =""
        for i in s:
            if i == "#":
                if sr:
                    sr = sr[:-1:]
            else:
                sr+=i
        for i in t:
            if i == "#":
                if tr:
                    tr = tr[:-1:]
            else:
                tr+=i
        return tr == sr
        