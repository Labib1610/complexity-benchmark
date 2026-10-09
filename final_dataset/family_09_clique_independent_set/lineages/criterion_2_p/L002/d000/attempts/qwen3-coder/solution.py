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
    
    color = [-1] * (n + 1)  # -1: unvisited, 0: color A, 1: color B
    
    # Check if graph is bipartite and find partitions
    partition_a = []
    partition_b = []
    
    for start in range(1, n + 1):
        if color[start] == -1:  # Unvisited node
            queue = deque([start])
            color[start] = 0
            partition_a.append(start)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        if color[neighbor] == 0:
                            partition_a.append(neighbor)
                        else:
                            partition_b.append(neighbor)
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Not bipartite - but problem guarantees it is
                        return None, None
    
    return partition_a, partition_b

def solve():
    n, m, k, edges = read_input()
    
    # Special case: no edges
    if m == 0:
        if k <= n:
            print("YES")
            print(" ".join(map(str, range(1, min(k + 1, n + 1)))))
        else:
            print("NO")
        return
    
    # Partition nodes into two sets
    partition_a, partition_b = bipartite_partition(n, edges)
    
    # Choose the larger partition if we can take all of it, or the smaller one if it fits exactly
    if len(partition_a) >= k:
        print("YES")
        print(" ".join(map(str, partition_a[:k])))
    elif len(partition_b) >= k:
        print("YES")
        print(" ".join(map(str, partition_b[:k])))
    elif len(partition_a) + len(partition_b) >= k and (len(partition_a) < k or len(partition_b) < k):
        # We need to take from both partitions - this would cause conflicts
        print("NO")
    else:
        print("NO")

solve()