import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    return n, m, k, edges, graph

def bipartite_partition(n, graph):
    # Color nodes with 0 or 1 using BFS
    colors = [-1] * (n + 1)  # index 0 unused
    for start in range(1, n + 1):
        if colors[start] == -1:
            queue = deque([start])
            colors[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == -1:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        # Not bipartite, but problem guarantees it is
                        pass
    # Partition into two sets
    set0 = [i for i in range(1, n + 1) if colors[i] == 0]
    set1 = [i for i in range(1, n + 1) if colors[i] == 1]
    return set0, set1

def solve():
    n, m, k, edges, graph = read_input()
    
    # Since the graph is guaranteed to have hidden codes where sum is odd,
    # it must be bipartite (edges connect nodes of different parity)
    set0, set1 = bipartite_partition(n, graph)
    
    # Choose the larger set to maximize possible k
    if len(set0) >= k:
        print("YES")
        print(' '.join(map(str, set0[:k])))
    elif len(set1) >= k:
        print("YES")
        print(' '.join(map(str, set1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()