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
    
    # BFS to get parent relationships and order
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    order = []
    root = 1
    for i in range(1, n + 1):
        if adj[i]:
            root = i
            break
    
    q = deque([root])
    parent[root] = 0
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if parent[v] == 0 and v != root:
                parent[v] = u
                children[u].append(v)
                q.append(v)
    
    # Sort children by subtree size (heavier first)
    size = [1] * (n + 1)
    for u in reversed(order):
        for v in children[u]:
            size[u] += size[v]
    
    for u in range(1, n + 1):
        children[u].sort(key=lambda x: -size[x])
    
    # Linear arrangement
    pos = [0] * (n + 1)
    current_pos = 1
    
    stack = [root]
    while stack:
        u = stack.pop()
        pos[u] = current_pos
        current_pos += 1
        for v in reversed(children[u]):
            stack.append(v)
    
    # Calculate total length
    total = 0
    for u in range(1, n + 1):
        for v in children[u]:
            total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(' '.join(map(str, pos[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()