class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                count_W = 0
                count_B = 0
                if grid[i][j] == 'W':
                    count_W+=1
                else:
                    count_B+=1
                if grid[i+1][j] == 'W':
                    count_W+=1
                else:
                    count_B+=1
                if grid[i][j+1] == 'W':
                    count_W+=1
                else:
                    count_B+=1
                if grid[i+1][j+1] == 'W':
                    count_W+=1
                else:
                    count_B+=1
                if count_W >= 3 or count_B >= 3:
                    return True
        return False
            


        