class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        mask = 1
        for i in range(32):
            if (mask & n) != 0:
                ans += 1 << 31 - i;
            mask <<= 1;


        return ans