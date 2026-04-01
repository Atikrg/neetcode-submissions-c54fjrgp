class Solution:

    def palindromeString(self, s, left, right):
        count = 0
        n = len(s)

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            right += 1
            left -= 1

        return count


    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):

            count += self.palindromeString(s, i, i)
            count +=  self.palindromeString(s, i , i + 1)

        return count