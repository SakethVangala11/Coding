class Solution {
    public String findCommonResponse(List<List<String>> responses) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for(int i = 0; i<responses.size(); i++){
            HashSet<String> set = new HashSet<String>();
            for(int j = 0; j<responses.get(i).size(); j++){
                set.add(responses.get(i).get(j));
            }
            for(String s: set){
                map.put(s, map.getOrDefault(s,0)+1);
            }
        }
        int max=0;
        String key = "";
        for(Map.Entry<String, Integer> m:map.entrySet()){
            if(max<m.getValue()){
                key=m.getKey();
                max=m.getValue();
            }else if(max == m.getValue()){
                if(key.compareTo(m.getKey())>0){
                    key=m.getKey();
                    max=m.getValue();
                }
            }
        }
        return key;
    }
}