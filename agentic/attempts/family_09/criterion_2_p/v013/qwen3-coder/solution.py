import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, k, edges

def check_bipartite(n, edges):
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try to 2-color the graph
    color = [-1] * n  # -1: unvisited, 0: color A, 1: color B
    for i in range(n):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return None, None  # Not bipartite
    partition_a = [i for i in range(n) if color[i] == 0]
    partition_b = [i for i in range(n) if color[i] == 1]
    return partition_a, partition_b

def main():
    n, m, k, edges = read_input()
    
    # Check if the graph is bipartite
    partition_a, partition_b = check_bipartite(n, edges)
    
    if partition_a is None:
        print("NO")
        return
    
    # Try to take k components from one of the partitions
    if len(partition_a) >= k:
        print("YES")
        result = [str(x + 1) for x in partition_a[:k]]  # Convert back to 1-indexed
        print(" ".join(result))
    elif len(partition_b) >= k:
        print("YES")
        result = [str(x + 1) for x in partition_b[:k]]  # Convert back to 1-indexed
        print(" ".join(result))
    else:
        print("NO")

if __name__ == "__main__":
    main()