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

            # Add character to window
            window[char] = window.get(char, 0) + 1

            # Character now satisfies its required frequency
            if char in targetFrequency and \
               window[char] == targetFrequency[char]:
                have += 1

            # Try shrinking window
            while have == need:

                # Update minimum window
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    result = s[left:right + 1]

                # Remove left character
                leftChar = s[left]

                window[leftChar] -= 1

                if leftChar in targetFrequency and \
                   window[leftChar] < targetFrequency[leftChar]:
                    have -= 1

                left += 1

        return result