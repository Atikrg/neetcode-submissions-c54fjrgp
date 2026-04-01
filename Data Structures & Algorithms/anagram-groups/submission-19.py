class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            char_count = [0] * 26

            for character in string:
                char_count[ord(character) - ord('a')]+=1


            result[tuple(char_count)].append(string);
        return result.values()