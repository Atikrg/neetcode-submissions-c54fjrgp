class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        maxi = nums[0];


        for i in range(len(nums)):
            total = total + nums[i]

            maxi = max(total, maxi)

            if total < 0:
                total = 0;

        return maxi