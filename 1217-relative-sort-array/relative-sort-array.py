class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        se = set(arr2)
        for i in arr1:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        ans = []
        for i in arr2:
            for j in range(d[i]):
                ans.append(i)
        rem = []
        for i in arr1:
            if i not in se:
                rem.append(i)
        rem.sort()
        ans.extend(rem)
        return ans
        

        