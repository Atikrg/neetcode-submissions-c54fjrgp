class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search = {}  # Use a dictionary to store value-to-index mapping
        for i in range(len(nums)):
            moreNeeded = target - nums[i]

            if moreNeeded in search:  # Check if the complement exists
                return [search[moreNeeded], i]  # Return indices of the two numbers

            search[nums[i]] = i  # Store the current number's index in the dictionary

        return [-1, -1]  # Return [-1, -1] if no solution exists