class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            se = set()
            for j in range(n):
                se.add(matrix[i][j])
            if len(se)!=n:
                return False
        
        for i in range(n):
            se = set()
            for j in range(n):
                se.add(matrix[j][i])
            if len(se)!=n:
                return False
        return True

        