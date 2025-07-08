class Solution {
    public int percentageLetter(String s, char letter) {
        int l = 0;
        int n = s.length();
        for(char c: s.toCharArray()){
            if(c == letter){
                l+=1;
            }
        }
        return (l*100)/n;
        
    }
}