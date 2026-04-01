class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the last seen index of each character
        left = 0  # Left boundary of the window
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1  # Move left pointer past the repeating character
            
            char_map[s[right]] = right  # Update last seen index of current character
            max_length = max(max_length, right - left + 1)  # Update max length
        
        return max_length



            
            




    