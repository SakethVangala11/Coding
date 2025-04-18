class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        int res = 0;
        int n = nums.length;
        for(int i=0; i<n-2;i++){
            for(int j=0; j<n-1; j++){
                for(int k=0; k<n; k++){
                    if(nums[j]-nums[i]==diff && nums[k]-nums[j]==diff){
                        res+=1;
                    }
                }
            }
        }
        return res;
    }
}