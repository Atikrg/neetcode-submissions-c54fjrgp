class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Create subarrays for cases: skip first house, skip last house
        skipLastHouse = nums[:-1]
        skipFirstHouse = nums[1:]

        # Calculate maximum loot for both cases
        lootSkippingFirstHouse = self.robHelper(skipFirstHouse)
        lootSkippingLastHouse = self.robHelper(skipLastHouse)

        # Return the maximum loot between the two cases
        return max(lootSkippingFirstHouse, lootSkippingLastHouse)

    def robHelper(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Initialize dp array
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Populate the dp array
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]