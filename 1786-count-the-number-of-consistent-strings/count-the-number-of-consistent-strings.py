class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        count = 0
        for i in words:
            flag = 1
            for j in i:
                if j not in s:
                    flag = 0
                    break
            if flag:
                count+=1
        return count
        