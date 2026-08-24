class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)


        for word in strs:
            char_counts = [0] * 26

            for character in word:
                char_counts[ord(character)- ord('a')]+=1


            result[tuple(char_counts)].append(word)


        return list(result.values())