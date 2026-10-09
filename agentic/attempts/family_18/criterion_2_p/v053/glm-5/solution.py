import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
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
    
    # BFS to find root and order
    root = 1
    parent = [0] * (n + 1)
    order = []
    q = deque([root])
    parent[root] = -1
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if parent[v] == 0:
                parent[v] = u
                q.append(v)
    
    # Greedy assignment: assign bays 1..n to nodes in BFS order
    assignment = [0] * (n + 1)
    for i, u in enumerate(order):
        assignment[u] = i + 1
    
    # Calculate total cable length
    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if v > u:  # count each edge once
                total += abs(assignment[u] - assignment[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()