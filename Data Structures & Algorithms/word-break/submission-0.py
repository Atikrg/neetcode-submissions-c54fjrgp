class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: empty string is always breakable

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and (s[i: i + len(w)] == w):  # Fixed condition
                    dp[i] = dp[i + len(w)]

                if dp[i]:  # Early stopping if we found a valid segmentation
                    break

        return dp[0]
