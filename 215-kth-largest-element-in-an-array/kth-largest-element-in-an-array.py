class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Heap Solution
        # pq= []
        # for i in nums:
        #     heapq.heappush(pq,-i)
        # while(k):
        #     x = heapq.heappop(pq)
        #     k-=1
        # return -x

        #QuickSelect solution
        # k=len(nums)-k
        # def quickSelect(l,r):
        #     p, pivot = l, nums[r]
        #     for i in range(l,r):
        #         if nums[i]<=pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p+=1
        #     nums[p], nums[r] = nums[r], nums[p]
        #     if p<k: return quickSelect(p+1,r)
        #     elif p>k: return quickSelect(l,p-1)
        #     else: return nums[p]
        # return quickSelect(0,len(nums)-1)

        #Sorting solution
        nums.sort()
        return nums[len(nums)-k]


        