class Solution {
    public boolean checkString(String s) {
        Boolean flag = false;
        for(int i = 0; i< s.length(); i++){
            if(s.charAt(i) == 'b') {
                flag = true;
            }
            if(flag && s.charAt(i) == 'a'){
                return false;
            }
        }
        return true;

    }
}