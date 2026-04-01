class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []


        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1


        for num, count in frequency.items():
            bucket[count].append(num)


        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
    