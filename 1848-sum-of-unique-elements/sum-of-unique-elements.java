class Solution {
    public int sumOfUnique(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int res = 0;
        for(int i = 0; i< nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i],0)+1);
        }
        for(Integer i: map.keySet()) {
            if(map.get(i) == 1) {
                res+=i;
            }
        }
        return res;
    }
}