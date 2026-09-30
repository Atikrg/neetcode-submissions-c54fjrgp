class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxJump = 0

        for i in range(len(nums)):

            jump = i + nums[i]
            if i > maxJump:
                return False


            maxJump = max(jump, maxJump)

            if maxJump >= len(nums) - 1:
                return True

        return False