class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1, d2 = {}, {}
        ans1, ans2 =0, 0
        for i in nums1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in nums2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        for i in d1:
            if i in d2:
                ans1+=d1[i]
        for i in d2:
            if i in d1:
                ans2+=d2[i]
        return [ans1, ans2]
        
        