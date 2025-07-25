class Solution {
    public int countGoodSubstrings(String s) {
        int count = 0;
        if(s.length() < 3) {
            return 0;
        }
        char a = s.charAt(0);
        char b = s.charAt(1);
        char c = s.charAt(2);
        for(int i = 3; i < s.length(); i++) {
            if(a!=b && b!=c && c!=a){
                count+=1;
            }
            a = b;
            b = c;
            c = s.charAt(i);
        }
        if(a!=b && b!=c && c!=a){
                count+=1;
            }
        return count;
    }
}