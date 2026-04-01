class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = 0
        total = 0
        maximum_nums = nums[0]
        for i in range(len(nums)):
            total += nums[i]

            maximum_nums = max(maximum_nums, total)
            if total < 0:
                total = 0


        return maximum_nums

