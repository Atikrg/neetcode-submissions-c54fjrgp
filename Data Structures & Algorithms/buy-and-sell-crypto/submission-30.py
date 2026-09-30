class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        profit = 0
        mini = float("inf")
        cost = 0


        for i in range(len(prices)):

            profit = prices[i] - mini
            cost = max(profit, cost)
            mini = min(mini, prices[i])

        return cost