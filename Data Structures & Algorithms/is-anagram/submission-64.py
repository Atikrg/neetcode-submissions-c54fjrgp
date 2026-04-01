class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts = [0] * 26

        for i in range(len(s)):
            char_counts[ord('a') - ord(s[i])] += 1
            char_counts[ord('a') - ord(t[i])] -= 1


        for i in char_counts:
            if i > 0:
                return False
        return True