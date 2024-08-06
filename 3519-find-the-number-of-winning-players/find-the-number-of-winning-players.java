class Solution {
    public int winningPlayerCount(int n, int[][] pick) {
        Map<Integer, Map<Integer, Integer>> map = new HashMap<>();
        for(int i = 0;i<n;i++){
            map.put(i, new HashMap<>());
        }

        for(int[] p:pick){
            int x = p[0], y = p[1];
            map.get(x).put(y,map.get(x).getOrDefault(y,0)+1);
        }

        int res = 0;
        for(int key:map.keySet()){
            Map<Integer, Integer> m  = map.get(key);
            for(int k:m.keySet()){
                if(m.get(k) > key){
                    res++;
                    break;
                }
            }
        }

        
    return res; 
    }
}