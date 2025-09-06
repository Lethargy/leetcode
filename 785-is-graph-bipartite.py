# https://leetcode.com/problems/is-graph-bipartite/

from typing import List
from collections import deque

# DFS

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False] * n
        group = [None] * n

        def dfs(node, count):
            group[node] = 'A' if count % 2 == 0 else 'B'
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, count + 1)

        for i in range(n):
            if not visited[i]:
                dfs(i,0)
                
        for node in range(n):
            for neighbor in graph[node]:
                if group[node] == group[neighbor]:
                    return False
        return True

# BFS

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False] * n
        group = [None] * n

        count = 0

        while not all(visited):
            queue = deque([visited.index(False)])

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    group[node] = 'A' if count % 2 == 0 else 'B'

                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                    
                    visited[node] = True
                
                count = count + 1
                
        for node in range(n):
            for neighbor in graph[node]:
                if group[node] == group[neighbor]:
                    return False
        
        return True