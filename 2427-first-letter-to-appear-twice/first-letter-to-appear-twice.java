class Solution {
    public char repeatedCharacter(String s) {
        HashSet<Character> set = new HashSet<Character>();
        int n = s.length();
        for(int i =0;i<n; i++){
            if(!set.contains(s.charAt(i))){
                set.add(s.charAt(i));
            }else{
                return s.charAt(i);
            }
        }
        return 'a';
    }
}