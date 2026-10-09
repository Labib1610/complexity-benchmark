import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
        B = int(next(it))
    except StopIteration:
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS to find connected components and build a spanning tree
    visited = [False] * (n + 1)
    tree_edges = []
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            queue = deque([i])
            visited[i] = True
            while queue:
                u = queue.popleft()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        tree_edges.append((u, v))
                        queue.append(v)
            components.append(comp)
    
    # Sort components by size (descending) to place larger components first
    components.sort(key=len, reverse=True)
    
    # Assign positions: 1, 2, ..., n
    assignment = [0] * (n + 1)
    pos = 1
    for comp in components:
        for u in comp:
            assignment[u] = pos
            pos += 1
    
    # Calculate total cost
    total_cost = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:  # Count each edge once
                total_cost += abs(assignment[u] - assignment[v])
    
    if total_cost <= B:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()