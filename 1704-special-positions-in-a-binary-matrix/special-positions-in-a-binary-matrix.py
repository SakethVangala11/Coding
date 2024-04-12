class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rowCount  = []
        colCount = []
        for i in range(m):
            count  = 0
            for j in range(n):
                if mat[i][j] == 1:
                    count+=1
            rowCount.append(count)
        
        for i in range(n):
            count = 0
            for j in range(m):
                if mat[j][i] == 1:
                    count+=1 
            colCount.append(count)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if rowCount[i] == 1 and colCount[j] == 1:
                        ans+=1
        return ans
                    
        