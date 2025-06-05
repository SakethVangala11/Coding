class Solution {
    public int maximizeSum(int[] nums, int k) {
        int maxi = 0;
        for(int i = 0; i< nums.length; i++) {
            if(nums[i] > maxi) {
                maxi = nums[i];
            }
        }
        return (maxi*k + (k*(k-1)/2));
    }
}