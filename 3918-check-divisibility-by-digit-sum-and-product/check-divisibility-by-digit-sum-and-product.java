class Solution {
    public boolean checkDivisibility(int n) {
        int num = n;
        int sum = 0;
        int product = 1;
        while(n>0) {
            int rem = n%10;
            sum+=rem;
            product*=rem;
            n/=10;
        }
        int sumo = sum+product;
        System.out.println(sumo);
        if(num%sumo == 0){
            return true;
        }
        return false;
    }
}