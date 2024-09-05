class Solution {
    public int generateKey(int num1, int num2, int num3) {
        int res = 0;
        int i = 0;
        while(num1>0 && num2>0 && num3>0){
            int rem1 = num1%10;
            num1 = num1/10;

            int rem2 = num2%10;
            num2 = num2/10;

            int rem3 = num3%10;
            num3 = num3/10;

            int mini = Math.min(rem1, Math.min(rem2,rem3));
            res+= Math.pow(10,i) * mini;
            i+=1;
            
        }  
        return res;
    }
}

