        #len(s) - freq <= 2
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        maxLength = 0
        mpp = {}
        maxFreq = 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            mpp[char] = 1 + mpp.get(char, 0 ) 
            maxFreq = max(maxFreq,mpp[char])


            length = right - left + 1
            
            if(length - maxFreq > k):
                leftchar = s[left]
                mpp[s[left]]-=1
                left +=1
            
            maxLength = max(maxLength, right - left + 1)
        return maxLength

