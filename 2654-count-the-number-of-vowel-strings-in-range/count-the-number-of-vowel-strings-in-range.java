class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        int res = 0;
        HashSet<Character> set = new HashSet<>(Arrays.asList('a','e','i','o','u'));
        for(int i=left; i<=right; i++){
            String word = words[i];
            int n = word.length();
            if(set.contains(word.charAt(0)) && set.contains(word.charAt(n-1))){
                res+=1;
            }
        }
        return res;
    }
}