class Solution {
    public long minCuttingCost(int n, int m, int k) {
        long ans=0;
        if(n<=k && m<=k) {
            return 0;
        }
        if(n>k && m<=k) {
            ans+=(long) (n-k)*k;
        }
        if(m>k && n<=k) {
            ans+=(long) (m-k)*k;
        }
        return ans;
    }
}