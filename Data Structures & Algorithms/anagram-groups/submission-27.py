class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  # Frequency count for a-z

            for c in s:
                count[ord(c) - ord("a")] += 1  # Map character to index

            res[tuple(count)].append(s)  # Use tuple(count) as hashable key

        return list(res.values())  # Convert dict_values to list before returning
