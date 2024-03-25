class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        d = 0
        for i in instructions:
            if i == 'G':
                if d == 0:
                    y+=1
                elif d == 1:
                    x+=1
                elif d == 2:
                    y-=1
                elif d == 3:
                    x-=1
            if i == 'L':
                d = (d-1)%4
            elif i == 'R':
                d = (d+1)%4         
        return (x,y) == (0,0) or d!=0    