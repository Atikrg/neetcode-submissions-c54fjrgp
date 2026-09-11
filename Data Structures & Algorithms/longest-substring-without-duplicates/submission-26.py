class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = float("-inf")


        mpp = {}

        left = 0

        for right in range(len(s)):

            if s[right] in mpp and mpp[s[right]] >= left:
                left = mpp[s[right]] + 1 

            
         
            mpp[s[right]] = right

            length = right - left + 1
            maxLength = max(length, maxLength)


        return maxLength if maxLength != float("-inf") else 0