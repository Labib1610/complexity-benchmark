import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def build_graph(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def is_bipartite(graph, n):
    color = {}
    for start in range(1, n + 1):
        if start not in color:
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False, {}
    return True, color

def solve():
    n, m, k, edges = read_input()
    graph = build_graph(n, edges)
    
    # Check if the graph is bipartite
    is_bip, coloring = is_bipartite(graph, n)
    
    if not is_bip:
        print("NO")
        return
    
    # Separate nodes into two sets based on bipartition
    set_a = [node for node in range(1, n + 1) if coloring.get(node, 0) == 0]
    set_b = [node for node in range(1, n + 1) if coloring.get(node, 0) == 1]
    
    # Choose the set that allows us to select exactly k nodes
    if len(set_a) >= k:
        selected = set_a[:k]
        print("YES")
        print(' '.join(map(str, selected)))
    elif len(set_b) >= k:
        selected = set_b[:k]
        print("YES")
        print(' '.join(map(str, selected)))
    else:
        print("NO")

solve()