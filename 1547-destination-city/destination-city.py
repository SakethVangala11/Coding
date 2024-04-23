class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set()
        destinations = set()

        for i in paths:
            sources.add(i[0])
            destinations.add(i[1])
        ans = (destinations - sources).pop()
        return ans
        
        

        