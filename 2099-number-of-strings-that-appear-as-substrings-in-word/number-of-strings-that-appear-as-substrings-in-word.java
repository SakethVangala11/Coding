class Solution {
    public int numOfStrings(String[] patterns, String word) {
        HashSet<String> substrings = new HashSet<>();
        int n = word.length();
        for(int i = 0; i<n; i++){
            String s = "";
            for(int j = i; j<n; j++) {
                s+=word.charAt(j);
                substrings.add(s);
            }
        }
        int res = 0;
        for(int i = 0; i<patterns.length; i++){
            if(substrings.contains(patterns[i])){
                res+=1;
            }
        }
        return res;
    }
}