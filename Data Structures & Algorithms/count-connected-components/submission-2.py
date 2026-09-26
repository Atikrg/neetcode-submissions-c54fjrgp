class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        counter = 0
        visited = [0] * n
        
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node):
            visited[node] = 1
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for i in range(n):
            if visited[i] == 0:
                counter += 1
                dfs(i)
        
        return counter




