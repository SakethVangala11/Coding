class Solution {
    public int[] minCosts(int[] cost) {
        int mini = cost[0];
        int n = cost.length;
        int result[] = new int[n];
        for(int i=0; i<n; i++){
            mini = Math.min(mini, cost[i]);
            result[i] = mini;
        }
        return result;
    }
}