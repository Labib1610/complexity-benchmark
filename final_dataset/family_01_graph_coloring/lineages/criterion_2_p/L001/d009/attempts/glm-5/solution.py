import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    parent = [-1] * n
    order = []
    is_bipartite = True
    
    for start in range(n):
        if color[start] == 0:
            color[start] = 1
            parent[start] = -1
            stack = [start]
            while stack:
                u = stack.pop()
                order.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        parent[v] = u
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
    
    if not is_bipartite:
        print("NO")
        return
    
    # Build tree structure
    children = [[] for _ in range(n)]
    for v in range(n):
        p = parent[v]
        if p != -1:
            children[p].append(v)
    
    # Process in reverse BFS order (reverse of order)
    cnt = [0] * n
    for u in reversed(order):
        c = 0
        for v in children[u]:
            c ^= cnt[v]
        cnt[u] = c
    
    # Find root of each component
    is_root = [False] * n
    for v in range(n):
        if parent[v] == -1:
            is_root[v] = True
    
    # Process in BFS order
    flip = [0] * n
    for u in order:
        if is_root[u]:
            flip[u] = cnt[u]
        else:
            p = parent[u]
            if cnt[u] == 1:
                flip[u] = flip[p] ^ 1
            else:
                flip[u] = flip[p]
    
    ans = []
    for i in range(n):
        if color[i] == 1:
            ans.append(1 if flip[i] == 0 else 2)
        else:
            ans.append(2 if flip[i] == 0 else 1)
    
    print("YES")
    print(' '.join(map(str, ans)))

solve()