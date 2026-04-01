class Solution:
    def reverseBits(self, n: int) -> int:
        
        mask = 1

        res = 0
        for i in range(32):
            if(mask & n) != 0:
                res +=  1  << 31 - i

            mask <<= 1

        return res