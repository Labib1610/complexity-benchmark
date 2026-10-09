import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def bipartite_check(n, edges):
    # Create adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: -1 unvisited, 0 color1, 1 color2
    color = [-1] * (n + 1)
    
    # Check if graph is bipartite
    for i in range(1, n + 1):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return None, None  # Not bipartite
    
    # Separate nodes into two sets
    set1 = [i for i in range(1, n + 1) if color[i] == 0]
    set2 = [i for i in range(1, n + 1) if color[i] == 1]
    
    return set1, set2

def solve():
    n, m, k, edges = read_input()
    
    if m == 0:
        # No conflicts, just pick any k modules
        print("YES")
        print(' '.join(map(str, range(1, k + 1))))
        return
    
    # Check if the graph is bipartite and get the two sets
    set1, set2 = bipartite_check(n, edges)
    
    if set1 is None:
        # This shouldn't happen according to problem statement
        print("NO")
        return
    
    # Try to select k nodes such that no two are connected
    # Since it's bipartite, we can take nodes from the same partition
    
    if len(set1) >= k:
        print("YES")
        print(' '.join(map(str, set1[:k])))
    elif len(set2) >= k:
        print("YES")
        print(' '.join(map(str, set2[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()