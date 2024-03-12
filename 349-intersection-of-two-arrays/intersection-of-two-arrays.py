class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set()
        for i in nums1:
            s1.add(i)
        res = set()
        for i in nums2:
            if i in s1:
                res.add(i)
        return list(res)
        