class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mpp = {}
        for i in range(len(nums)):
            moreNeeded = target - nums[i]

            if moreNeeded in mpp:
                return [mpp[moreNeeded], i]

            mpp[nums[i]] = i
            