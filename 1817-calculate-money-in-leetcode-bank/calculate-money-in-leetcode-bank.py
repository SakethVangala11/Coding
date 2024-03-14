class Solution:
    def totalMoney(self, n: int) -> int:
        rem  = n%7
        num = n//7
        sumo = num*(28)
        sumo+=(((num-1)*num)//2)*7
        sumo+=(rem*(rem+1))//2 + num*rem

        return sumo
        