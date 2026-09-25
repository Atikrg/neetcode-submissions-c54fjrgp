class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        freq = {}


        for num in nums:
            freq[num] = 1 + freq.get(num, 0)


        for key, values in freq.items():
            if values == 1:
                return key


        return -1


        