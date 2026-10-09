import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def bipartite_partition(n, edges):
    # Create adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = group A, -1 = group B
    color = [0] * (n + 1)
    
    # Check if bipartite and partition nodes
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # This shouldn't happen according to problem statement
                        return None, None
    
    group_a = [i for i in range(1, n + 1) if color[i] == 1]
    group_b = [i for i in range(1, n + 1) if color[i] == -1]
    
    return group_a, group_b

def solve():
    n, m, k, edges = read_input()
    
    # Since the graph is bipartite, we can partition it into two independent sets
    group_a, group_b = bipartite_partition(n, edges)
    
    # Choose the larger group to maximize our options
    if len(group_a) >= k:
        print("YES")
        print(*group_a[:k])
    elif len(group_b) >= k:
        print("YES")
        print(*group_b[:k])
    else:
        print("NO")

if __name__ == "__main__":
    solve()