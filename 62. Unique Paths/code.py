class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                top = dp[i-1][j] if i>0 else 0
                left = dp[i][j-1] if j>0 else 0
                dp[i][j] += top + left
        return dp[m-1][n-1]
                