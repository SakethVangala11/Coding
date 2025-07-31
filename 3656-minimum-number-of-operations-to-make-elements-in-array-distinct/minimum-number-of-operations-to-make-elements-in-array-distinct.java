class Solution {
    public int minimumOperations(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>();
        for (int i = nums.length-1; i>=0; i--) {
            if(!set.contains(nums[i])) {
                set.add(nums[i]);
            }
            else{
                System.out.println(i);
                return (i/3)+1;
            }
        }
        return 0;
    }
}