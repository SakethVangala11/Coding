class Solution {
    public boolean numberOfDigits(int num) {
        int digits = 0;
        while(num>0) {
            num/=10;
            digits+=1;
        }
        return digits%2==0;
    }

    public int findNumbers(int[] nums) {
        int count = 0;
        for(int i = 0; i< nums.length; i++) {
            if(numberOfDigits(nums[i])) {
                count+=1;
            }
        }
        return count;
    }
}