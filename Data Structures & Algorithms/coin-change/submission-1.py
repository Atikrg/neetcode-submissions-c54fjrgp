class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def minimum_elements_util(arr, ind, T, dp):
            # Base case: If we're at the first element
            if ind == 0:
                return T // arr[0] if T % arr[0] == 0 else float('inf')

            # If the result for this index and target sum is already calculated, return it
            if dp[ind][T] != -1:
                return dp[ind][T]

            # Calculate the minimum elements needed without taking the current element
            not_taken = minimum_elements_util(arr, ind - 1, T, dp)

            # Calculate the minimum elements needed by taking the current element
            taken = float('inf')
            if arr[ind] <= T:
                taken = 1 + minimum_elements_util(arr, ind, T - arr[ind], dp)

            # Store the minimum of 'not_taken' and 'taken' in the DP array and return it
            dp[ind][T] = min(not_taken, taken)
            return dp[ind][T]

        if amount == 0:
            return 0

        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]  # Initialize DP table with -1

        ans = minimum_elements_util(coins, n - 1, amount, dp)
        return -1 if ans == float('inf') else ans
