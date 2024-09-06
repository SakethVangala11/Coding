class Solution {
    public int countKConstraintSubstrings(String s, int k) {
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            int a = 0;
            int b = 0;
            for(int j = i; j<s.length(); j++){
                if(s.charAt(j) == '0'){
                    a+=1;
                }else{
                    b+=1;
                }
                if(a<=k || b<=k){
                    count+=1;
                }
            }
        }
        return count;

    }
}