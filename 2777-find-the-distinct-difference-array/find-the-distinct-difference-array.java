class Solution {
    public int[] distinctDifferenceArray(int[] nums) {
        int n= nums.length;
        int[] prefix = new int[n];
        int[] suffix = new int[n];
        int[] result = new int[n];
        HashSet<Integer> prefixSet = new HashSet<Integer>();
        HashSet<Integer> suffixSet = new HashSet<Integer>();
        for(int i = 0; i< n; i++) {
            if(!prefixSet.contains(nums[i])){
                prefixSet.add(nums[i]);
            }
            prefix[i] = prefixSet.size();
        }
        for(int i = n-1; i>=0; i-- ){
            if(!suffixSet.contains(nums[i])){
            suffixSet.add(nums[i]);
            }
            suffix[i] = suffixSet.size();
        }
        for(int i = 0; i<n-1; i++) {
            result[i] = prefix[i] - suffix[i+1];
        }
        result[n-1] = prefix[n-1];
        return result;

    }
}