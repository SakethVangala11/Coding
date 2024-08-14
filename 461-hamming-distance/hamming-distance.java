class Solution {
    public int hammingDistance(int x, int y) {
        int count = 0;
        int res = x^y;
        System.out.println(res);
        for(int i = 0; i<32; i++){
            if((res & 1<<i)>0){
                count+=1;
            }
        }
     return count;   
    }
}