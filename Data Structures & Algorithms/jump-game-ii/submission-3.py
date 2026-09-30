class Solution:
    def jump(self, nums: List[int]) -> int:
        

        jumps = 0
        current = 0
        far = 0

        for i in range(len(nums) -1):
            far = max(far, i + nums[i])

            if i == current:
                jumps += 1
                current = far

        return jumps