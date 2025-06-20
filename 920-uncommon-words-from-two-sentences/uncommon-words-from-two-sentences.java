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
        for(Map.Entry<String,Integer> entry: map.entrySet()){
            if(entry.getValue() == 1){
                result.add(entry.getKey());
            }
        }
        return result.toArray(new String[0]);
    }
}