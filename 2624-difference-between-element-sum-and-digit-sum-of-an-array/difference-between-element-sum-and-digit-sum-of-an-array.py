class Solution:
    def sumo_digit(self, num):
        sumo = 0
        while(num>0):
            rem = num%10
            sumo+=rem
            num//=10
        return sumo

    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        for i in nums:
            digit_sum+=self.sumo_digit(i)
        return abs(sum(nums)-digit_sum)
   