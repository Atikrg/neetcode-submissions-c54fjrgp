class Solution:

    def expandAroundCenter(self, s, left ,right):

        max_length = 0
        
        substring = ""

        while left >= 0 and right < len(s) and s[left] == s[right]:

            if (right - left + 1 > max_length):
                max_length = right - left + 1

                substring = s[left: right + 1]

            left -= 1
            right += 1

        return substring    
    

    def longestPalindrome(self, s: str) -> str:
        result = ""
        
        for i in range(len(s)):
            odd = self.expandAroundCenter(s, i, i)
            even = self.expandAroundCenter(s, i , i + 1)

            if len(odd) > len(result):
                result = odd

            if(len(even) > len(result)):
                result = even


        return result
        