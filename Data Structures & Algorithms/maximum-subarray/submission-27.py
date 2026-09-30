class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        total = 0
        maximum = float("-inf")

        for i in range(len(nums)):

            total += nums[i]

            maximum = max(maximum, total)

            if total < 0:
                total = 0

        return maximum