class Solution {
    public int reverseDegree(String s) {
        int sumo = 0;
        for(int i=0; i<s.length(); i++){
            int ch = s.charAt(i);
            sumo+= (26 - (ch - 97))*(i+1);
        }
        return sumo;
    }
}