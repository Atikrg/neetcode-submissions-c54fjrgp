class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0


        setter = set(nums)

        longest = 0


        for i in range(len(nums)):
            if nums[i] in setter:
                currentNum = nums[i]
                streak = 1

                while currentNum + 1 in nums:
                    currentNum += 1
                    streak += 1

                longest = max(longest, streak)

        return longest