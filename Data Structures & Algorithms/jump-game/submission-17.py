class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxLength = 0;


        n = len(nums)


        for i in range(len(nums)):

            if i > maxLength:
                return False;
            
            jump = i + nums[i]

            maxLength = max(maxLength, jump)

            if maxLength >= n - 1:
                return True

        return False
            
