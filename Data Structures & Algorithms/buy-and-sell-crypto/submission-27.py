class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = float("inf")
        maxi = float("-inf")

        profit = 0
        cost = 0

        for i in range(len(prices)):

            profit = prices[i] - mini

            cost = max(profit , cost)

            mini = min(mini, prices[i])

        
        return cost
