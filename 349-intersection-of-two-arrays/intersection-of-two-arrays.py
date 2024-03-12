class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        for i in nums1:
            s1.add(i)
        for i in nums2:
            s2.add(i)
        res = []
        for i in s1:
            if i in s2:
                res.append(i)
        return res
        