class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesrow, zeroesrow, onescol, zeroescol = [], [], [], []
        for i in range(len(grid)):
            count_o = 0
            count_z = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count_z+=1
                else:
                    count_o+=1
            onesrow.append(count_o)
            zeroesrow.append(count_z)
        
        for i in range(len(grid[0])):
            count_o = 0
            count_z = 0
            for j in range(len(grid)):
                if grid[j][i] == 0:
                    count_z+=1
                else:
                    count_o+=1
            onescol.append(count_o)
            zeroescol.append(count_z)
        
        diff = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(diff)):
            for j in range(len(diff[0])):
                diff[i][j] = onesrow[i] + onescol[j] - zeroesrow[i] - zeroescol[j]
        
        return diff  