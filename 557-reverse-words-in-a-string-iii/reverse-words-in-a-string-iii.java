class Solution {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();
        StringBuilder word = new StringBuilder();
        for(char ch: s.toCharArray()){
            if(ch == ' '){
                res.append(word.reverse());
                res.append(' ');
                word.setLength(0);
            } else{
                word.append(ch);
            }
        }
        res.append(word.reverse());
        return res.toString();
    }
}