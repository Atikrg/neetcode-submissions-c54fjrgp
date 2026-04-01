class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total_sum:int = 0

        maxLength: int = nums[0];
        for i in range(0,len(nums)):
            
            total_sum = total_sum + nums[i]

            maxLength = max(maxLength,total_sum)


            if total_sum < 0:
                total_sum = 0;

        return maxLength