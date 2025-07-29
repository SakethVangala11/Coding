class Solution {
    public boolean digitCount(String num) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0;i < num.length(); i++) {
            int n = num.charAt(i) - '0';
            map.put(n,map.getOrDefault(n, 0)+1);
        }
        for(int i = 0; i< num.length(); i++) {
            int n = num.charAt(i) - '0';
            int freq = map.getOrDefault(i,0);
            if(freq!=n) {
                return false;
            }     
        }
        return true;
    }
}