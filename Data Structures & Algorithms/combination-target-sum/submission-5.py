class Solution:

    def helper(self, result, nums, path, target, i):

        if target == 0:
            result.append(path.copy())
            return

        if i >= len(nums) or target < 0:
            return

        # Take nums[i]
        path.append(nums[i])
        self.helper(result, nums, path, target - nums[i], i)
        path.pop()

        # Skip nums[i]
        self.helper(result, nums, path, target, i + 1)


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        self.helper(result, nums, [], target, 0)

        return result