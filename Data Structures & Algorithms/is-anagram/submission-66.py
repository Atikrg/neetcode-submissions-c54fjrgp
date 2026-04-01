class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            char_counts[ord('a') - ord(s[i])] += 1
            char_counts[ord('a') - ord(t[i])] -= 1


        for count in char_counts:
            if count > 0:
                return False
        return True