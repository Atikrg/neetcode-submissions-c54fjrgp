class Solution {
    reverseBits(n) {
        let mask = 1;
        let ans = 0;

        for (let i = 0; i < 32; i++) {
            if ((mask & n) !== 0) {
                ans += 1 << (31 - i);
            }
            mask <<= 1;
        }

        return ans >>> 0;
    }
}
