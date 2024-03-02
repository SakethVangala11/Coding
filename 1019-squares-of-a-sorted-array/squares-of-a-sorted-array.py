import heapq
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            heapq.heappush(result, i*i)
        ans = []
        while(result):
            x = heapq.heappop(result)
            ans.append(x)
        return ans
        