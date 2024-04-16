class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}

        for i in words:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j] = 1
        
        n = len(words)
        for i in d:
            if d[i]%n != 0:
                return False
        return True

        