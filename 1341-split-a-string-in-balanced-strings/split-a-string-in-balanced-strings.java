class Solution {
    public int balancedStringSplit(String s) {
        int l = 0;
        int r = 0;
        int n = s.length();
        int ans = 0;
        for(int i=0; i<n; i++) {
            if(s.charAt(i) == 'L'){
                l+=1;
            }else{
                r+=1;
            }
            if(r>0 && l>0 && l==r) {
                ans+=1;
                l=0;
                r=0;
            }
        }
        return ans;
    }
}