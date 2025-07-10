class Solution {
    public int countGoodSubstrings(String s) {
        int count = 0;
        for(int i = 0; i < s.length()-2; i++) {
            int res = 0;
            HashSet<Character> set = new HashSet<Character>();
            for(int j = i; j < i+3; j++){
                set.add(s.charAt(j));
            }
            if(set.size() == 3){
                System.out.println(i);
                count+=1;
            }
        }
        return count;
    }
}