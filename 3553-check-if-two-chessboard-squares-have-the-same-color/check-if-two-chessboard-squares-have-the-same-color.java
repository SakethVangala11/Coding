class Solution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        int c11 = coordinate1.charAt(0);
        int c21 =  coordinate2.charAt(0);
        int c12 = (int) coordinate1.charAt(1);
        int c22 = (int) coordinate2.charAt(1);

        if(((c11 + c12)%2 == 0 && (c21+c22)%2 ==0) || ((c11 + c12)%2 == 1 && (c21+c22)%2 ==1)){
            return true;
        }
        return false;
    }
}