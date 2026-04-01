class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0;
        
        longest_streak = 0;

        for num in nums:
                current_streak = 1
                currentNumber = num

                while currentNumber + 1 in nums:
                    current_streak +=1
                    currentNumber += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak    