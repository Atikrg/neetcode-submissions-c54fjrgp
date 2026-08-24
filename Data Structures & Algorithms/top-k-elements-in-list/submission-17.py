class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]

        frequency = {}

        result = []


        for num in nums:
            frequency[num] = 1+ frequency.get(num, 0)


        for key, values in frequency.items():

            bucket[values].append(key)


        for i in range(len(bucket) - 1, 0, -1):
            for element in bucket[i]:
                result.append(element)
                if len(result) == k:
                    return result

        return result