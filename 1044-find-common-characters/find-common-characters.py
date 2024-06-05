class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])
        l = []
        for i in words:
            d = {}
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j] = 1
            l.append(d)
        res = []
        dic = l[0]
        for i in dic:
            mini = dic[i] 
            for j in range(1, len(l)):
                if i in l[j]:
                    mini = min(mini, l[j][i])
                elif i not in l[j]:
                    mini = 0
                    break
            print(i, mini)
            for j in range(mini):
                res.append(i)         
        return res









        