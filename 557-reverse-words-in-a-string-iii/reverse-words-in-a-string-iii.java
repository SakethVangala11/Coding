class Solution {
    public String reverseWords(String s) {
        Stack<Character> stack = new Stack<>();
        int n = s.length();
        String res = new String("");
        for(int i=0; i<n; i++) {
            Character ch = s.charAt(i);
            if(ch.equals(' ')){
                while(!stack.empty()){
                    Character c = stack.pop();
                    res+=c;
                }
                res+=" ";
            }
            else{
                stack.push(ch);
            }
        }
        while(!stack.empty()){
            Character c = stack.pop();
            res+=c;
        }
        return res;
    }
}