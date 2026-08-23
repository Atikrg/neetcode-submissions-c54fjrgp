class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = 0

        maxi = float("-inf")


        for i in nums:
            total += i

            maxi = max(total, maxi)

            if total < 0:
                total = 0


        return maxi