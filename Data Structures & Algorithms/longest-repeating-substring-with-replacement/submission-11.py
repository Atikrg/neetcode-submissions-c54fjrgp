class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        char_set = {}
        maxFreq = 0
        length = 0
        maxLength = 0
        left = 0
        right = 0

        for right in range(len(s)):  # Iterate using right pointer
            char = s[right]
            char_set[char] = char_set.get(char, 0) + 1
            maxFreq = max(maxFreq, char_set[char])  # Update max frequency
            
            length = right - left + 1
            if(length - maxFreq > k):
                leftChar = s[left]
                char_set[s[left]] -= 1 
                left+=1

            length = right - left + 1
            maxLength = max(maxLength,length)
        return maxLength
