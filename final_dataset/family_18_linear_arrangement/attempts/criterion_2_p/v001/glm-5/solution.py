import sys
from sys import setrecursionlimit

def solve():
    data = sys.stdin.buffer.read().split()
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
    
    if B < n - 1:
        sys.stdout.write("NO\n")
        return
    
    setrecursionlimit(max(10000, 4 * n))
    pos = [0] * (n + 1)
    order = []
    visited = bytearray(n + 1)
    
    # Iterative DFS to build preorder
    root = 1
    stack = [root]
    visited[root] = 1
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = 1
                stack.append(v)
    
    for i, u in enumerate(order):
        pos[u] = i + 1
    
    out = ["YES"]
    out.append(" ".join(str(pos[i]) for i in range(1, n + 1)))
    sys.stdout.write("\n".join(out) + "\n")

solve()