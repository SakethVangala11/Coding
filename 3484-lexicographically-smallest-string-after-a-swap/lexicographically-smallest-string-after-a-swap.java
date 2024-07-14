class Solution {
    public String getSmallestString(String s) {
        char[] chr = s.toCharArray();
        String mini = s;
        int n = s.length();
        for(int i=0;i<n-1;i++){
            if((chr[i]%2==0 && chr[i+1]%2==0) || (chr[i]%2==1 && chr[i+1]%2==1)){
            char[] ch = s.toCharArray();
            char temp = ch[i];
            ch[i] = ch[i+1];
            ch[i+1] = temp;
            String str = new String(ch);
            System.out.println(str);
            if(str.compareTo(mini) < 0 ){
                mini = str;
            }
            }
        }
        return mini;
        
    }
}