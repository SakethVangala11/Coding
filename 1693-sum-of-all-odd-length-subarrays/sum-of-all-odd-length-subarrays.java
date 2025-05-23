class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int ans = 0;
        int n = arr.length;
        for(int i = 0; i < n; i++) {
            int res = 0;
            for(int j = i; j < n; j++) {
                res+=arr[j];
                if((j-i+1)%2==1) {
                    ans+=res;
                }
            }
        }
        return ans;
    }
}