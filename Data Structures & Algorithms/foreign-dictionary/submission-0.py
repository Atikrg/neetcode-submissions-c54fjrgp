from collections import deque
from typing import List


class Solution:

    def topologicalSort(self, graph, indegrees, chars):
        q = deque()

        # Add all characters with indegree 0
        for ch in chars:
            if indegrees[ch] == 0:
                q.append(ch)

        result = []

        while q:
            node = q.popleft()
            result.append(node)

            for neighbor in graph[node]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    q.append(neighbor)

        # Cycle exists
        if len(result) != len(chars):
            return ""

        return "".join(result)

    def foreignDictionary(self, words: List[str]) -> str:

        # Collect all unique characters
        chars = set()

        for word in words:
            for ch in word:
                chars.add(ch)

        # Graph: character -> characters that come after it
        graph = {ch: [] for ch in chars}

        # Indegree of every character
        indegrees = {ch: 0 for ch in chars}

        # Build graph by comparing adjacent words
        for i in range(len(words) - 1):

            s1 = words[i]
            s2 = words[i + 1]

            length = min(len(s1), len(s2))

            found_difference = False

            for j in range(length):

                if s1[j] != s2[j]:

                    u = s1[j]
                    v = s2[j]

                    # Avoid duplicate edges
                    if v not in graph[u]:
                        graph[u].append(v)
                        indegrees[v] += 1

                    found_difference = True
                    break

            # Invalid ordering:
            # ["abc", "ab"]
            if not found_difference and len(s1) > len(s2):
                return ""

        return self.topologicalSort(graph, indegrees, chars)