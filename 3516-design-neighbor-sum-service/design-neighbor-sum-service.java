class NeighborSum {
    int[][] grid = new int[10][10];
    int i = 0, j = 0;

    public NeighborSum(int[][] grid) {
            this.grid = grid;
            return;
    }

    public void helper(int value){
        for(i = 0; i < grid.length; i++){
            for(j = 0; j<grid.length; j++){
                if(grid[i][j] == value){
                    this.i = i;
                    this.j = j;
                    return;
                }
            }
        }
    }
    
    public int adjacentSum(int value) {
        int sum = 0;
        helper(value);
        if(i!=0){
            sum+=grid[i-1][j];
        }
        if(j!=0){
            sum+=grid[i][j-1];
        }
        if(i!=grid.length-1){
            sum+=grid[i+1][j];
        }
        if(j!=grid.length-1){
            sum+=grid[i][j+1];
        }
        return sum; 
    }
    
    public int diagonalSum(int value) {
        int sum = 0;
        helper(value);
        if(i>0 && j>0){
            sum+=grid[i-1][j-1];
        }
        if(i<grid.length-1 && j<grid.length-1){
            sum+=grid[i+1][j+1];
        }
        if(i>0 &&j<grid.length-1){
            sum+=grid[i-1][j+1];
        }
        if(i<grid.length-1 && j>0){
            sum+=grid[i+1][j-1];
        }
        return sum;
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = new NeighborSum(grid);
 * int param_1 = obj.adjacentSum(value);
 * int param_2 = obj.diagonalSum(value);
 */