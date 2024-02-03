class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
        s={'b','a','l','o','n'}
        for i in text:
            if i in s:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        if len(d)!=5:
            return 0
        d['l'] = d['l']//2
        d['o'] = d['o']//2
        
        mini = len(text)
        for i in d:
            if d[i]<mini:
                mini = d[i]
        return mini
                
   
        