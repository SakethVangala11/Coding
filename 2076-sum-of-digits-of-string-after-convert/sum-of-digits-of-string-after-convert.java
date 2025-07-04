class Solution {
    public String sumOfDigits(String num){
        int res = 0;
        for(char c: num.toCharArray()){
            res+= c-'0';
        }
        return String.valueOf(res);
    }
    public int getLucky(String s, int k) {
        StringBuilder number = new StringBuilder("");
        for(char c: s.toCharArray()){
            number.append((int) c - 96);
        }
        String num = number.toString();
        while(k > 0){
            String ans = sumOfDigits(num);
            num = ans;
            k-=1;
        }
        return Integer.parseInt(num);
    }
}