class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False


        maxLength = 0

        for i in range(len(nums)):

            if i > maxLength:
                return False

            jump = i + nums[i]
            maxLength = max(maxLength, jump)



        return True