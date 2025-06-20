class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for(String word: s1.split(" ")){
            map.put(word, map.getOrDefault(word,0)+1);
        }
        for(String word: s2.split(" ")){
            map.put(word, map.getOrDefault(word,0)+1);
        }
        ArrayList<String> result = new ArrayList<String>();
        for(String key: map.keySet()){
            Integer value = map.get(key);
            if(value == 1){
                result.add(key);
            }
        }
        String[] ans = result.stream().toArray(String[]::new);
        return ans;
    }
}