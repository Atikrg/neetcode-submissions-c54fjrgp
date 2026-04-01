class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1

        for i in range(32):
            if (mask & n )!= 0:
                bits += 1
            mask = mask << 1
        return bits