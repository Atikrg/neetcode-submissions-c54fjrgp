class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        total = 0
        for num in nums:
            total = total + num
            maxi = max(total, maxi)
            if total < 0:
                total = 0
        return maxi 