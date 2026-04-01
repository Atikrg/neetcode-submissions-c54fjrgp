class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
    
        # Create DP array
        min_coins_dp = [float('inf')] * (amount + 1)
        min_coins_dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    min_coins_dp[i] = min(min_coins_dp[i], 1 + min_coins_dp[i - coin])
        
        return -1 if min_coins_dp[amount] == float('inf') else min_coins_dp[amount]
