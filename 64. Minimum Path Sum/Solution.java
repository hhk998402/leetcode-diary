class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int dp[][] = new int[m][n];

        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                int val1 = Integer.MAX_VALUE;
                int val2 = Integer.MAX_VALUE;
                boolean oneValueSet = false;
                if(i-1 >= 0){
                    val1 = dp[i-1][j];
                    oneValueSet = true;
                }
                if(j-1 >= 0){
                    val2 = dp[i][j-1];
                    oneValueSet = true;
                }
                dp[i][j] = grid[i][j] + (oneValueSet ? Math.min(val1, val2) : 0);
            }
        }

        for(int i = 0; i<m;i++){
            for(int j = 0;j<n;j++){
                System.out.print(dp[i][j]);
            }
            System.out.println("");
        }
        return dp[m-1][n-1];
    }
}