class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ele = -1 
        count = 0
        n = len(arr)
        threshold = n//4

        for i in arr:
            if i!=ele:
                ele = i
                count=1
            else:
                count+=1
            if count>threshold:
                    return ele
        