class Solution {
    public int fib(int n) {
        int a = 0;
        int b = 1;
        int c = 0;
        if(n == 0){
            return a;
        }else if( n == 1){
            return b;
        }
        while(n > 1){
            c = a+b;
            a = b;
            b = c;
            n-=1;
        }
        return c;
    }
}