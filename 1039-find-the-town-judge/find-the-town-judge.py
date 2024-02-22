class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        rows,cols = (n,n)
        arr = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in trust:
            x, y = i[0], i[1]
            arr[x-1][y-1] = 1
        judge = []
        for j in range(cols):
            count = 0
            for i in range(rows):
                if i==j and arr[i][j]==1:
                    break
                elif i!=j and arr[i][j]==1:
                    count+=1
            if count == n-1:
                judge.append(j)
        for i in judge:
            count = 0
            for value in arr[i]:
                if value!=0:
                    break
                count+=1
            if count == n:
                return i+1


        return -1