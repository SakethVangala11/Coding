class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        l = [0]*(n+1)
        r = [0]*(n+1)
        c1 = 0
        c2 = 0
        for i in range(n):
            if customers[i] == 'N':
                l[i] = c1
                c1+=1
            else:
                l[i] = c1
        l[-1] = c1
        for i in range(n-1,-1,-1):
            if customers[i] == 'Y':
                c2+=1
                r[i]=c2
            else:
                r[i] = c2
        mini = float('inf')
        idx = 0
        total = [0]*(n+1)
        for i in range(n+1):
            total[i] = l[i]+r[i]
            if total[i] < mini:
                mini = total[i]
                idx = i  
        return idx
            

        