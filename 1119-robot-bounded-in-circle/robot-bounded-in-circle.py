class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        d = 'N'
        for i in instructions:
            if i == 'G':
                match d:
                    case 'N':
                        y+=1
                    case 'S':
                        y-=1
                    case 'W':
                        x-=1
                    case 'E':
                        x+=1
            else:
                if i=='L':
                    match d:
                        case 'N':
                            d = 'W'
                        case 'W':
                            d = 'S'
                        case 'S':
                            d = 'E'
                        case 'E':
                            d = 'N'
                if i == 'R':
                    match d:
                        case 'N':
                            d = 'E'
                        case 'E':
                            d = 'S'
                        case 'S':
                            d = 'W'
                        case 'W':
                            d = 'N'
        if x==0 and y==0:
            return True
        if d == 'N':
            return False
        return True
        


    
        