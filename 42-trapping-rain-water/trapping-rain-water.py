class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0]*len(height)
        r = [0]*len(height)
        sumo = 0
        lhigh = height[0]
        rhigh = height[-1]

        for i in range(1, len(height)):
            l[i] = lhigh
            lhigh = max(lhigh, height[i])
        for i in range(len(height)-2,-1,-1):
            r[i] = rhigh
            rhigh = max(rhigh, height[i])
        
        for i in range(len(height)):
            if min(l[i],r[i]) - height[i] > 0:
                sumo+= min(l[i],r[i]) - height[i]
        return sumo
        
        
        

        







        
        