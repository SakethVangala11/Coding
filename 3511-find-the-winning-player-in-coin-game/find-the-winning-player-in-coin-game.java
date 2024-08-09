class Solution {
    public String losingPlayer(int x, int y) {
        int i = 0;
        while(true){
            if(x>=1 && y>=4){
                x-=1;
                y-=4;
            }else{
                if(i%2==0){
                    return "Bob";
                }
                return "Alice";
            }
            i+=1;
        }
    }
}