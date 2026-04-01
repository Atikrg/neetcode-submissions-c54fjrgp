class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            required = target - nums[i]

            if required in res:
                return [res[required], i]

            res[nums[i]] = i
 
            



        

            