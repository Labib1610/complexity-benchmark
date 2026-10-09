import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS to find connected components
    visited = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            q = deque([i])
            visited[i] = True
            while q:
                u = q.popleft()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            components.append(comp)
    
    # Sort components by size (largest first)
    components.sort(key=len, reverse=True)
    
    # Assign slots: components are placed in contiguous blocks
    # Units within a component are placed consecutively
    assignment = [0] * (n + 1)
    current_slot = 1
    
    for comp in components:
        for u in comp:
            assignment[u] = current_slot
            current_slot += 1
    
    # Calculate total wire length
    total_length = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:  # Count each edge once
                total_length += abs(assignment[u] - assignment[v])
    
    if total_length <= B:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()