class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0;

        longest = 0
        for num in nums:
            current_streak = 1
            currentNum = num

            while currentNum + 1 in nums:
                current_streak += 1
                currentNum += 1

            longest = max(current_streak, longest)
        return longest