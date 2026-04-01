class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}
        result = []
        bucket = [[] for _ in range(len(nums) + 1) ]

        for i in range(len(nums)):
            frequency[nums[i]] = 1 + frequency.get(nums[i], 0)

        for key, values in frequency.items():
            bucket[values].append(key)


        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)


                if len(result) == k:
                    return result

        return result
