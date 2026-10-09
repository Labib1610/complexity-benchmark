import sys

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
        x = int(next(it))
        y = int(next(it))
        adj[x].append(y)
        adj[y].append(x)
    
    # Greedy: place highest-degree vertex at center, then neighbors adjacent, etc.
    # We'll use a BFS-like layering from the highest-degree vertex.
    deg = [0] * (n + 1)
    for v in range(1, n + 1):
        deg[v] = len(adj[v])
    
    root = max(range(1, n + 1), key=lambda v: deg[v])
    
    # BFS from root
    from collections import deque
    order = []
    visited = [False] * (n + 1)
    q = deque([root])
    visited[root] = True
    while q:
        v = q.popleft()
        order.append(v)
        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                q.append(u)
    
    # Assign positions: root at center, then alternate left/right
    pos = [0] * (n + 1)
    center = (n + 1) // 2
    pos[order[0]] = center
    left = center - 1
    right = center + 1
    for v in order[1:]:
        if left >= 1:
            pos[v] = left
            left -= 1
        else:
            pos[v] = right
            right += 1
    
    total = 0
    for v in range(1, n + 1):
        for u in adj[v]:
            if u > v:
                total += abs(pos[v] - pos[u])
    
    if total <= B:
        print("YES")
        print(' '.join(str(pos[v]) for v in range(1, n + 1)))
    else:
        print("NO")

solve()