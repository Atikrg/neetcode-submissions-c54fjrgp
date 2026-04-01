class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(s, left, right):
                subString = ''
                max_length = 0;


                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if(right - left + 1 > max_length):
                        max_length = right - left + 1
                        subString = s[left : right + 1]
                    left -= 1
                    right += 1

                return subString;

        result = ''

        for i in range(len(s)):
            odd = expandAroundCenter(s, i, i)
            even =  expandAroundCenter(s, i , i+ 1)


            if len(odd) > len(result):
                result = odd

            if len(even) > len(result):
                result = even

        return result;