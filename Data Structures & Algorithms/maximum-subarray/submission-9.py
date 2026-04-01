class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        maxLength = nums[0]

        for i in range(len(nums)):
            total = total + nums[i]

            maxLength = max(total, maxLength)

            if total < 0:
                total = 0

        return maxLength