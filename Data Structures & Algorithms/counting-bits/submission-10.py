class Solution:
    def countBits(self, n: int) -> List[int]:
        res: list = [0] * (n + 1)

        for i in range(1, n + 1):

            res[i] = res[i // 2] + (i % 2)

        return res

