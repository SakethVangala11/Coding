class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]
        r=[1]
        answer=[]
        pre=1
        post=1
        for i in range(0,len(nums)):
            pre*=nums[i]
            l.append(pre)
        for i in range(len(nums)-1,-1,-1):
            post*=nums[i]
            r.append(post)
        print(l,r)
        for i in range(len(nums)):
            answer.append(l[i]*r[len(nums)-i-1])
        return answer



    
        
        








        
        