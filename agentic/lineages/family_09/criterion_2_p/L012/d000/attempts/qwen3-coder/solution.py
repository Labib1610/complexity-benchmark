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

def bipartite_partition(n, graph):
    color = [-1] * (n + 1)  # -1: unvisited, 0: group A, 1: group B
    
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # This should not happen according to problem statement
                        # but we handle it just in case
                        return None, None
                        
    group_a = [i for i in range(1, n + 1) if color[i] == 0]
    group_b = [i for i in range(1, n + 1) if color[i] == 1]
    
    return group_a, group_b

def solve():
    n, m, k, edges = read_input()
    graph = build_graph(n, edges)
    
    # Since the graph is bipartite, we can partition nodes into two groups
    group_a, group_b = bipartite_partition(n, graph)
    
    # Check which group(s) we can take nodes from
    if len(group_a) >= k:
        selected = group_a[:k]
        print("YES")
        print(*selected)
    elif len(group_b) >= k:
        selected = group_b[:k]
        print("YES")
        print(*selected)
    else:
        print("NO")

solve()