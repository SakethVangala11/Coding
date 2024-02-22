class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0]*(n+1)
        for x,y in trust:
            trusted[x]-=1
            trusted[y]+=1
        for i in range(1,n+1):
            if trusted[i]==n-1:
                return i
        return -1


        #Bruteforce
        # rows,cols = (n,n)
        # arr = [[0 for _ in range(cols)] for _ in range(rows)]
        # for i in trust:
        #     x, y = i[0], i[1]
        #     arr[x-1][y-1] = 1
        # judge = []
        # for j in range(cols):
        #     count = 0
        #     for i in range(rows):
        #         if i==j and arr[i][j]==1:
        #             break
        #         elif i!=j and arr[i][j]==1:
        #             count+=1
        #     if count == n-1:
        #         judge.append(j)
        # for i in judge:
        #     count = 0
        #     for value in arr[i]:
        #         if value!=0:
        #             break
        #         count+=1
        #     if count == n:
        #         return i+1
        # return -1