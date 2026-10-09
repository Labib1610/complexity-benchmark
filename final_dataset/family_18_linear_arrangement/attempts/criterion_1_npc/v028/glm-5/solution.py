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
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # BFS-based topological sort by degree (smallest degree first)
    order = []
    q = deque()
    in_queue = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)
            in_queue[i] = True
    
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            degree[v] -= 1
            if degree[v] == 0 and not in_queue[v]:
                q.append(v)
                in_queue[v] = True
    
    # Assign phases: first in order gets phase 1, etc.
    phase = [0] * (n + 1)
    for idx, node in enumerate(order):
        phase[node] = idx + 1
    
    # Calculate total degradation
    total = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:
                total += abs(phase[u] - phase[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, phase[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()