from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(len(prices) - 1):  # Consider `i` as the buying day
            for j in range(i + 1, len(prices)):  # Consider `j` as the selling day
                # Calculate profit by selling on day `j` after buying on day `i`
                current_profit = prices[j] - prices[i]
                # Update the maximum profit
                profit = max(profit, current_profit)
        
        return profit
