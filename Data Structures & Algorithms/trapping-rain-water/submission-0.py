class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n == 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        rightMax[n - 1] = height[n - 1]

        # Build left maximum array
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        # Build right maximum array
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        totalWater = 0

        # Calculate trapped water
        for i in range(n):
            totalWater += min(leftMax[i], rightMax[i]) - height[i]

        return totalWater