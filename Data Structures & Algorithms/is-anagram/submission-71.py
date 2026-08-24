class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        if not s or not t:
            return False


        if len(s) != len(t):
            return False


        char_counts = [0] * 26



        for i in range(len(s)):
            char_counts[ord(s[i]) - ord('a')] += 1
            char_counts[ord(t[i]) - ord('a')] -= 1

        for count in char_counts:
            if count >= 1:
                return False

        return True

    