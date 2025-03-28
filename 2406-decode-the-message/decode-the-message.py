class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        idx = 0
        for i in key:
            if i == ' ':
                continue
            if i not in d:
                d[i] = idx
                idx+=1
        res = ""
        for i in message:
            if i == " ":
                res+=" "
            else:
                res+=chr(98+d[i]-1)
        return res
        
            

        