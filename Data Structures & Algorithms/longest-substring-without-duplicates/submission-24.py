class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        frequency = {}
        maxLength = 0
        left = 0


        for right in range(len(s)):
            if s[right] in frequency and frequency[s[right]]>= left:
                left = frequency[s[right]] + 1



            frequency[s[right]] = right


            maxLength = max(maxLength, right - left + 1)


        return maxLength