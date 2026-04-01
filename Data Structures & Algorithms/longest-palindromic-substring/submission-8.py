class Solution:

    def expandAroundCenter(self, s, left, right):
        maxLength = 0
        subString = ''

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1 > maxLength):
                maxLength = right - left + 1
                subString = s[left:right + 1]

            left -= 1
            right +=1
        return subString


    def longestPalindrome(self, s: str) -> str:
        result = ''

        for i in range(len(s)):
            odd = self.expandAroundCenter(s, i, i)
            even = self.expandAroundCenter(s, i, i + 1)

            if len(odd) > len(result):
                result = odd  # ✅ Updates result instead of returning early

            if len(even) > len(result):
                result = even  # ✅ Updates result instead of returning early

        return result