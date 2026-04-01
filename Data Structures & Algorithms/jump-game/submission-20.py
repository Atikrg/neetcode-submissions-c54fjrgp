class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        for i in range(len(nums)):

            if i > maxJump:
                return False
            jump = i + nums[i]
            maxJump = max(maxJump, jump)


            if maxJump >= len(nums) - 1:
                return True
        return False

