class Solution {
    public int maximum69Number (int num) {
        String str = String.valueOf(num);
        String res = "";
        int flag = 1;
        int i = 0;

        while(i < str.length() ) {
            if(flag == 1 && (str.charAt(i)) == '6') {
                res+="9";
                flag = 0;
            } else{
                res+=str.charAt(i);
            }
            i+=1;
        }
        
        return Integer.parseInt(res);
        
    }
}