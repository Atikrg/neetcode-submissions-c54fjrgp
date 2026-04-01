class Solution:
    def rob(self, nums: List[int]) -> int:


        if len(nums) == 1:
            return nums[0]


        if len(nums) == 2:
            return max(nums[0], nums[1])

        
        skipFirst = nums[:-1];
        skipLast = nums[1:]


        lootSkippingFirstHouse = self.robHelper(skipFirst)
        lootSkippingLastHouse = self.robHelper(skipLast)


        return max(lootSkippingFirstHouse, lootSkippingLastHouse)

    def robHelper(self, nums):

        if len(nums) == 1:
            return nums[0]


        if len(nums) == 2:
            return max(nums[0], nums[1])

        loot = [0] * (len(nums))

        loot[0] = nums[0]
        loot[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            loot[i] = max(loot[i - 2] + nums[i], loot[i - 1])


        return loot[-1]