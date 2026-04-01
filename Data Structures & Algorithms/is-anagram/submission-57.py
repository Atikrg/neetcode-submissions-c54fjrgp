class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  # Anagrams must have the same length

        char_counts = [0] * 26  # Array for counting characters

        for i in range(len(s)):
            char_counts[ord(s[i]) - ord('a')] += 1  # Increment count for `s`
            char_counts[ord(t[i]) - ord('a')] -= 1  # Decrement count for `t`

        for count in char_counts:
            if count != 0:  # All counts should be zero if `s` and `t` are anagrams
                return False

        return True
