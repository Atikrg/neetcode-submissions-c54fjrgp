class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}

        left = 0
        maxLength = 0

        for right in range(len(s)):
            if s[right] in freq and freq[s[right]] >= left:
                left = freq[s[right]] + 1

            freq[s[right]] = right

            maxLength = max(maxLength,right - left + 1)
        return maxLength
            