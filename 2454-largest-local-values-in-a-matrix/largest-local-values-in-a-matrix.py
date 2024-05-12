class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []
        for i in range(n-2):
            temp = []
            for j in range(n-2):
                maxi = -1
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        maxi = max(maxi, grid[a][b])
                temp.append(maxi)
            ans.append(temp)
        return ans
                
                





        