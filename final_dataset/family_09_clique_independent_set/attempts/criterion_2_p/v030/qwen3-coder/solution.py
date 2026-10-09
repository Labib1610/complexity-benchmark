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
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def bipartite_partition(n, adj):
    # Try to partition the graph into two sets (coloring with 2 colors)
    color = [-1] * (n + 1)  # -1: unvisited, 0: set A, 1: set B
    
    for start in range(1, n + 1):
        if color[start] == -1:  # Unvisited node
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # This should not happen according to problem statement
                        # but we'll handle it just in case
                        return None, None
    
    set_a = [i for i in range(1, n + 1) if color[i] == 0]
    set_b = [i for i in range(1, n + 1) if color[i] == 1]
    
    return set_a, set_b

def solve():
    n, m, k, edges = read_input()
    adj = build_graph(n, edges)
    
    # Partition into two sets (since it's bipartite)
    set_a, set_b = bipartite_partition(n, adj)
    
    if set_a is None:  # Not bipartite - shouldn't happen per problem statement
        print("NO")
        return
    
    # Check if we can form a safe collection of size k
    # A safe collection is any subset of processes from the same set
    if len(set_a) >= k:
        print("YES")
        print(' '.join(map(str, set_a[:k])))
    elif len(set_b) >= k:
        print("YES")
        print(' '.join(map(str, set_b[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()