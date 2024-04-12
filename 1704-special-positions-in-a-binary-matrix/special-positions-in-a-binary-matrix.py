class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        count = 0
        for i in range(m):
            for j in range(n):
                flag = 0
                if mat[i][j]==1:
                    for a in range(n):
                        if a == j:
                            continue
                        if mat[i][a] == 1:
                            flag = 1
                            break
                    for a in range(m):
                        if a == i:
                            continue
                        if mat[a][j] == 1:
                            flag = 1
                            break
                    if flag == 0:  
                        count+=1
        return count
                    
        