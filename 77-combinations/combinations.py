class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        candidates = []
        for i in range(1,n+1):
            candidates.append(i)
        
        def dfs(i,cur):
            if len(cur)==k:
                res.append(cur.copy())
                return
            
            if i>=len(candidates):
                return 
            
            cur.append(candidates[i])
            dfs(i+1,cur)

            cur.pop()
            dfs(i+1,cur)
        dfs(0,[])
        return res
            
                
        