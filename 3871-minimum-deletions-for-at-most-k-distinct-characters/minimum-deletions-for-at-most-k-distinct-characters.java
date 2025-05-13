class Solution {
    public int minDeletion(String s, int k) {
        HashMap<Character, Integer> map = new HashMap<>();
        int deletions = 0;
        for(int i=0; i<s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i),0)+1);
        }
        ArrayList<Integer> values = new ArrayList<>(map.values());
        values.sort(null);
        int n = values.size() - k;
        for(int i=0; i<n; i++) {
            deletions+=values.get(i);
        }
        return deletions;
    }
}
