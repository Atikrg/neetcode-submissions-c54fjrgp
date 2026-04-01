class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = prices[0]

        profit = 0

        maxi = 0


        for i in range(1, len(prices)):
            cost =  prices[i] - mini
            profit = max(profit, cost)
            mini = min(prices[i], mini)

        return profit