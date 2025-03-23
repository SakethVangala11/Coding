class Solution:
    def sumOfMultiples(self, n: int) -> int:
        arr = [False]*1001
        for i in range(1, len(arr)):
            if i%3==0 or i%5==0 or i%7==0:
                arr[i]=True
        sumo = 0 
        for i in range(1,n+1):
            if arr[i]:
                sumo+=i
        return sumo

        