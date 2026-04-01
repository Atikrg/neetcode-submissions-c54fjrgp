class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        mini = prices[0]
        for i in range(len(prices)):
            cost = prices[i] - mini
            profit = max(profit, cost)
            mini = min(prices[i], mini)


        return profit


