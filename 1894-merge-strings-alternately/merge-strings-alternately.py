class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        count=0
        res=''
        while i<len(word1) and j<len(word2):
            if count%2==0:
                res+=word1[i]
                i+=1
            else:
                res+=word2[j]
                j+=1
            count+=1
        while(i<len(word1)):
            res+=word1[i]
            i+=1
        while(j<len(word2)):
            res+=word2[j]
            j+=1
        return res


        