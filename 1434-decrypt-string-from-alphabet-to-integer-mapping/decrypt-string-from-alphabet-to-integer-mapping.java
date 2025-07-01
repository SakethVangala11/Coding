class Solution {
    public String freqAlphabets(String s) {
        StringBuilder res = new StringBuilder("");
        int n = s.length();
        int i = 0;
        while(i<n){
            if(i+2 < n && s.charAt(i+2) == '#'){
                String a = "" + s.charAt(i) + s.charAt(i+1);
                char c = (char) (Integer.parseInt(a) + 96);
                res.append(c);
                i+=3;
            }
            else {
                String a = "" + s.charAt(i);
                char c = (char) (Integer.parseInt(a) + 96);
                res.append(c);
                i+=1;
            }
        }
        return res.toString();
    }
}