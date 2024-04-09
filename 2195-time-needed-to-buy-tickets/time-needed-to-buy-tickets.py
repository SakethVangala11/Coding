class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sumo = 0
        target = tickets[k]
        for i in tickets:
            if i<target:
                sumo+=i
            else:
                sumo+=target
        
        i = k+1
        while(i<len(tickets)):
            if tickets[i]>=target:
                sumo-=1
            i+=1
        return sumo


        
        

        