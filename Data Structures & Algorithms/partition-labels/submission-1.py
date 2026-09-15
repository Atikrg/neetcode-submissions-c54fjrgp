class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        partitions = []

        i = 0

        while i < len(s):

            start_index = i
            end_index = s.rfind(s[start_index])

            j = start_index + 1

            while j < end_index:

                last_index_of_next_char = s.rfind(s[j])

                if last_index_of_next_char > end_index:
                    end_index = last_index_of_next_char

                j += 1

            partitions.append(end_index - start_index + 1)

            i = end_index + 1

        return partitions