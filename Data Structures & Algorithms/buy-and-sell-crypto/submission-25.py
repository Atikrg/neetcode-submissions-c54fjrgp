class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        maxi = float('-inf')

        mini = float("inf")
        cost = 0
        
        for i in range(len(prices)):
            profit = prices[i] - mini
            cost = max(profit, cost)
            mini = min(prices[i], mini)


        return cost;
