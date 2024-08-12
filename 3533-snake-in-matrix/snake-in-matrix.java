class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        int i = 0, j = 0;
        for(String c: commands){
            if(c.equals("UP")){

                i-=1;
            }else if(c.equals("DOWN")){
                i+=1;
            }else if(c.equals("LEFT")){
                j-=1;
            }else if(c.equals("RIGHT")){
                j+=1;
            }    
        }

        return (i*n)+j;
        
    }
}