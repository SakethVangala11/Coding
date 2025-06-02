class Solution {
    public int findGCD(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int min = nums[0];
        int max = nums[n-1];
        for(int i = min; i>0; i--){
            if(max%i==0 && min%i==0){
                return i;
            }
        }
        return 1;
    }
}