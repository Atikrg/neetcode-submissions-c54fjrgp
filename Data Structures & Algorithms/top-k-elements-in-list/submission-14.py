class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bubbles = [[] for _ in range(len(nums) + 1) ]

        freq = {}
        res = []


        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        for key, values in freq.items():
            bubbles[values].append(key)


        for i in range(len(bubbles)-1,0,-1):
            for num in bubbles[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return res



