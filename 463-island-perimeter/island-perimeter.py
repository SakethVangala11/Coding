class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perm  = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perm+=4
                    if i>0 and grid[i-1][j] == 1:
                        perm-=1
                    if i<row-1 and grid[i+1][j] == 1:
                        perm-=1
                    if j>0 and grid[i][j-1] == 1:
                        perm-=1
                    if j<col-1 and grid[i][j+1] == 1:
                        perm-=1      
        return perm        