class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        maxLength = 0
        left = 0
        
        setMap = {}

        for right in range(len(s)):

            if s[right] in setMap and setMap[s[right]] >= left:
                left = setMap[s[right]] + 1

            setMap[s[right]] = right
            length = right - left + 1
            maxLength = max(maxLength, length)
        return maxLength

