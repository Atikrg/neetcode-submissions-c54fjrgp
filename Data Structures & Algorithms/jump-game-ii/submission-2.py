class Solution:
    def jump(self, nums: List[int]) -> int:
   

        jumps = 0

        farthestJump = 0
        currentEnd = 0


        for i in range(len(nums) - 1):

            farthestJump = max(farthestJump, i + nums[i])


            if i == currentEnd:

                jumps+=1
                currentEnd = farthestJump

        return jumps



# if i == currentEnd then increase the jump count and set the farthest
