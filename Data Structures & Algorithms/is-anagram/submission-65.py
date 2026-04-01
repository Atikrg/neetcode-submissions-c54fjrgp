class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        chars_count = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            chars_count[ord('a') - ord(s[i])] += 1
            chars_count[ord('a') - ord(t[i])] -= 1


        for i in chars_count:
            if i > 0:
                return False

        return True