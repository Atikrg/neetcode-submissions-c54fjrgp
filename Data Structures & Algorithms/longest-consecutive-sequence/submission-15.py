class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 0  # To track the longest streak found
        
        # Check each number in the list as a starting point
        for i in range(len(nums)):
            current_num = nums[i]
            current_streak = 1  # Every number is at least a streak of length 1
            
            # Start counting the streak for `current_num`
            while current_num + 1 in nums:  # If the next number exists, count it
                current_num += 1
                current_streak += 1
            
            # Update the longest streak found so far
            longest = max(longest, current_streak)
        
        return longest
