class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp = {}
        left = 0 
        maxLength = 0


        for i in range(len(s)):
            if s[i] in mpp and mpp[s[i]] >= left:
                left = mpp[s[i]] + 1

            mpp[s[i]] = i


            maxLength = max(maxLength, i - left + 1)

        return maxLength