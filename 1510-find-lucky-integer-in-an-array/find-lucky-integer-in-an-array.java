class Solution {
    public int findLucky(int[] arr) {
        int ans = -1;
        HashMap<Integer, Integer> freq = new HashMap<Integer, Integer>();
        int n = arr.length;
        for(int i = 0; i < n; i++){
            freq.put(arr[i], freq.getOrDefault(arr[i],0)+1);
        }
        for(Map.Entry<Integer, Integer> entry: freq.entrySet()){
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if(key == value){
                ans = Math.max(ans, key);
            }
        }
        return ans;
    }
}