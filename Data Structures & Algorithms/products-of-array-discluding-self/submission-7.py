class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        # Fill the left product array
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        # Fill the right product array
        for i in range(len(nums) - 2, -1, -1):  # Include 0 in the range
            right[i] = right[i + 1] * nums[i + 1]

        # Calculate the result using left and right products
        ans = [0] * len(nums)  # Initialize with the correct length
        for i in range(len(nums)):
            ans[i] = left[i] * right[i]

        return ans