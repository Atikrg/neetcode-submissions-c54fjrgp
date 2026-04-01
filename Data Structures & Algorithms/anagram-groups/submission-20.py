class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in strs:
            char_counts = [0] * 26

            for char in i:
                char_counts[ord(char) - ord('a')] += 1

            result[tuple(char_counts)].append(i)

        return result.values();