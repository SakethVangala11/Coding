class Solution {
    public int findGCD(int[] nums) {
        int n = nums.length;
        int max=0, min=1001;
        for(int i = 0; i<n; i++) {
            if(nums[i]>max){
                max=nums[i];
            }
            if(nums[i]<min){
                min = nums[i];
            }
        }
        for(int i = min; i>0; i--){
            if(max%i==0 && min%i==0){
                return i;
            }
        }
        return 1;
    }
}