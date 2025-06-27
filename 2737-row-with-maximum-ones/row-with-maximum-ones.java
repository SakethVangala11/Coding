class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int onesCount = 0;
        int row = 0;
        for(int i = 0; i< m; i++){
            int count = 0;
            for(int j = 0; j<n; j++){
                System.out.println(mat[i][j]);
                if(mat[i][j] == 1){
                    count+=1;
                }
            }
            if(count>onesCount){
                onesCount = count;
                row = i;
            }
        }
        int[] res = new int[2];
        res[0] = row;
        res[1] = onesCount;
        return res;
    }
}