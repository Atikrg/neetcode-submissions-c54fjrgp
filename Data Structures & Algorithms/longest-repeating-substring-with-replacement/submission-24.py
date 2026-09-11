class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxFrequency = 0
        length = 0
        maxLength = 0

        left = 0


        frequency = {}

        for right in range(len(s)):

            frequency[s[right]] = 1+ frequency.get(s[right] , 0)

            maxFrequency = max(maxFrequency, frequency[s[right]])


            length = right - left + 1


            if length - maxFrequency > k:
                frequency[s[left]] -= 1

                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength