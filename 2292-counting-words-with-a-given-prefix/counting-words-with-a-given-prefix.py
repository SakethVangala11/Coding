class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            flag = 1
            for i in range(len(pref)):
                if len(word)<len(pref):
                    flag = 0
                    break
                if pref[i] == word[i]:
                    pass
                else:
                    flag = 0
            if flag:
                count+=1
            

        return count


        