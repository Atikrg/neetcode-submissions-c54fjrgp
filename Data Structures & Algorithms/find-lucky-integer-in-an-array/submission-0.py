class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        for i in arr:
            freq[i] = 1 + freq.get(i, 0)

        res = -1

        for i, v in freq.items():
            if i == v:
                res = max(res, i)

        return res