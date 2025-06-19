class Solution {
    public int smallestNumber(int n) {
        int res = 0;
        for(int i = 0; i<=n; i++) {
            int x = (int) Math.pow(2,i);
            if(x > n){
                res = x;
                return res-1;
            }
        }
        return res-1;
    }
}