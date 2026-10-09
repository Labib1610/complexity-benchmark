import sys
from sys import stdin

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0]*(n+1)
    parent = [0]*(n+1)
    order = [0]*(n+1)
    depth = [0]*(n+1)
    cnt = 0
    stack = []
    
    for src in range(1, n+1):
        if color[src] == 0:
            color[src] = 1
            depth[src] = 0
            order[src] = cnt
            cnt += 1
            stack.append(src)
            while stack:
                u = stack.pop()
                cu = color[u]
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - cu
                        parent[v] = u
                        depth[v] = depth[u] + 1
                        order[v] = cnt
                        cnt += 1
                        stack.append(v)
                    elif color[v] == cu:
                        print("NO")
                        return
    
    # Build DFS tree adjacency
    tree_adj = [[] for _ in range(n+1)]
    for u in range(1, n+1):
        pu = parent[u]
        for v in adj[u]:
            if v != pu and parent[v] != u:
                if u < v:
                    tree_adj[u].append(v)
                    tree_adj[v].append(u)
    
    # Process back edges in reverse DFS order
    for u in range(n, 0, -1):
        for v in tree_adj[u]:
            if depth[u] > depth[v]:
                if color[u] == color[v]:
                    color[u] = 3 - color[u]
    
    out = ['YES']
    out.append(' '.join(str(color[i]) for i in range(1, n+1)))
    sys.stdout.write('\n'.join(out))

solve()