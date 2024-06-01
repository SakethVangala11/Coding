class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums2)
        mini = 12
        for i in nums1:
            if i in s:
                mini = min(mini, i)
        if mini!=12:
            return mini

        a = min(nums1)
        b = min(nums2)
        return min(int(str(a)+str(b)), int(str(b)+str(a)))
        