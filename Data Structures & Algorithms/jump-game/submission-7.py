
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxLength = 0
        n = len(nums)

        for i in range(n):
            if i > maxLength:
                return False
            
            maxLength = max(maxLength, i + nums[i])
            
            # If we can reach or surpass the last index
            if maxLength >= n - 1:
                return True

        return False
