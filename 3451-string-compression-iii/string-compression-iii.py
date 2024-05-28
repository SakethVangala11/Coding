class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        count = 1
        while(i<len(word)-1):
            if word[i]!= word[i+1]:
                if count:
                    comp+=str(count)
                    comp+=word[i]
                i+=1
                count = 1
            else:

                i+=1
                count+=1
                if count == 9:
                    comp+=str(count)
                    comp+=word[i]
                    count = 0
        if count:
            comp+=str(count)
            comp+=word[i]
            
        return comp

        