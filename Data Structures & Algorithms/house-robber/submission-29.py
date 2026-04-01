class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        loots = [0] * len(nums)

        loots[0] = nums[0]
        loots[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):

            loots[i] = max(loots[i - 2] + nums[i], loots[i - 1])

        return loots[-1]