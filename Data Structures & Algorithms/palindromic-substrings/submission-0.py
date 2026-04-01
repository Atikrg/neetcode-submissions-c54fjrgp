class Solution:
    def palindromeSubstring(self, s, left, right):
        count = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

        return count

    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            count += self.palindromeSubstring(s, i, i)    # Odd length palindromes
            count += self.palindromeSubstring(s, i, i+1)  # Even length palindromes

        return count
