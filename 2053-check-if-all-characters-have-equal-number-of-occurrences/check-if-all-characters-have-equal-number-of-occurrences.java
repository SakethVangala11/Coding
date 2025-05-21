class Solution {
    public boolean areOccurrencesEqual(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int n = s.length();
        for(int i = 0; i<n; i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i),0)+1);
        }
        int freq = map.get(s.charAt(0));
        for(char key: map.keySet()){
            if(map.get(key)!=freq) {
                return false;
            }
        }
        return true;
    }
}