class Solution:
    def customSortString(self, order: str, s: str) -> str:
        uniqueSet = set()
        for i in order:
            uniqueSet.add(i)
        s_dict = {}
        rest_seq = []
        for i in s:
            if i in s_dict:
                s_dict[i]+= 1
            else:
                s_dict[i] = 1
        print(uniqueSet,s_dict)
        ans = ""
        for i in s:
            if i not in uniqueSet:
                rest_seq.append(i)
        
        for i in order:
            if i in s_dict:
                ans+=i*s_dict[i]
        
        for i in rest_seq:
            ans+=i
        



        return ans

        
        