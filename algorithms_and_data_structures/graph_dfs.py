"""
Depth-First Search
https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
"""

graph = {
    "A": {"B", "C"},
    "B": {"A", "D", "E"},
    "C": {"A", "F"},
    "D": {"B"},
    "E": {"B", "F"},
    "F": {"C", "E"},
}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


visited = dfs(graph, start="A")
assert visited == {"E", "D", "F", "A", "C", "B"}