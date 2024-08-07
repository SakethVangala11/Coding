class Solution {
    public boolean canAliceWin(int[] nums) {
        int single = 0, doub = 0;
        for(int i:nums){
            if(i<10){
                single+=i;
            }else{
                doub+=i;
            }
        }
        if(single==doub){
            return false;
        }
        return true;    
    }
}