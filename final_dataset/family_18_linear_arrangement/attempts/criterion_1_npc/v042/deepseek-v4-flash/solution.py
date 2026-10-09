import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Greedy BFS ordering from highest degree vertex
    deg = [len(adj[i]) for i in range(n)]
    start = max(range(n), key=lambda i: deg[i])
    
    order = []
    visited = [False] * n
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        order.append(u)
        # sort neighbors by degree descending for better locality
        for v in sorted(adj[u], key=lambda x: -deg[x]):
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
    # Assign steps: place first in middle, then alternate left/right
    pos = [0] * n
    left = (n - 1) // 2
    right = left + 1
    for i, node in enumerate(order):
        if i % 2 == 0:
            pos[node] = left
            left -= 1
        else:
            pos[node] = right
            right += 1
    
    # Compute total cost
    total = 0
    for u, v in edges:
        total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(" ".join(str(pos[i] + 1) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()