class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D grid initialized with 1s
        grid = [[1] * n for _ in range(m)]

        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]  # Return the bottom-right corner value
