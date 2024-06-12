class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cuhr, cumin = current.split(":")
        cohr, comin = correct.split(":")
        cutot = int(cuhr)*60 + int(cumin)
        cotot = int(cohr)*60 + int(comin)
        diff = cotot - cutot
        op = 0
        while(diff):
            if diff>=60:
                diff-=60
                op+=1
            elif diff>=15:
                diff-=15
                op+=1
            elif diff>=5:
                diff-=5
                op+=1
            else:
                diff-=1
                op+=1
        return op




        


        