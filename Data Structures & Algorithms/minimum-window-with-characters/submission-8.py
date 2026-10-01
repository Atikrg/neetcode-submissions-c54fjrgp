class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t or not s:
            return ""


        targetFrequency = {}

        for char in t:
            targetFrequency[char] = targetFrequency.get(char, 0) + 1


        need = len(targetFrequency)
        have = 0

        window = {}


        left = 0

        minLength = float("inf")
        result = ""


        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1


            if char in targetFrequency and window[char] == targetFrequency[char]:
                have += 1


            while have == need:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    result = s[left:right + 1]

                leftChar = s[left]

                window[leftChar] -=1


                if leftChar in targetFrequency and window[leftChar] < targetFrequency[leftChar]:
                    have -= 1

                left += 1

        return result
