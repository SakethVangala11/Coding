class Solution {
    public String toLowerCase(String s) {
        StringBuilder res = new StringBuilder();
        for(int i=0; i<s.length(); i++){
            if ((int) s.charAt(i) >=65 && (int) s.charAt(i) <=90) {
                res.append((char) (s.charAt(i)+32));
            } else {
                res.append(s.charAt(i));
            }
        }
        return res.toString();
    }
}