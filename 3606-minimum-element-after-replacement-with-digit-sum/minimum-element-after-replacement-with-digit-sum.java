class Solution {
    public int sumOfDigits(int num){
        //logic for sum of digits of num
        int sum = 0;
        while(num>0){
            int rem = num%10;
            sum+=rem;
            num = num/10;
        }
        return sum;
    }
    public int minElement(int[] nums) {
        int mini = 10000;
        for(int i = 0; i < nums.length; i++){
            int res = sumOfDigits(nums[i]);
            if(res<mini){
                mini = res;
            }
        }
        return mini;   
    }
}