class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1, d2 = {}, {}
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
        ans = []
        for i in d1:
            if i in d2:
                count = min(d1[i], d2[i])
                for j in range(count):
                    ans.append(i)
        return ans
        