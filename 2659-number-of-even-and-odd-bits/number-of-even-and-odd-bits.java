class Solution {
    public int[] evenOddBit(int n) {
        int even = 0;
        int odd = 0;
        int[] res = new int[2];
        for(int i = 0; i < 32; i++) {
            if((1<<i & n) != 0) {
                if(i%2 == 0){
                    even+=1;
                }else{
                    odd+=1;
                }
            }
        }
        res[0] = even;
        res[1] = odd;
        return res;
    }
}