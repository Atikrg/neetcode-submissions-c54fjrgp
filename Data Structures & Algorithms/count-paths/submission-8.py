class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1


        dp = [[1] * m] * n


        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]