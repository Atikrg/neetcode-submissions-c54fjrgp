class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)


        for words in strs:
            char_counts = [0] * 26
            for character in words:
                char_counts[ord(character) - ord('a')] += 1


            result[tuple(char_counts)].append(words)


        return list(result.values())