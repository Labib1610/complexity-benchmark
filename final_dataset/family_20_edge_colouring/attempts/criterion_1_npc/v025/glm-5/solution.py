import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    color = [0] * m
    visited = [False] * (n + 1)
    
    for s in range(1, n + 1):
        if visited[s]:
            continue
        stack = [s]
        visited[s] = True
        while stack:
            u = stack.pop()
            used = set()
            for v, idx in adj[u]:
                if color[idx] != 0:
                    used.add(color[idx])
            avail = {1, 2, 3} - used
            for v, idx in adj[u]:
                if color[idx] == 0:
                    c = avail.pop()
                    color[idx] = c
                    used.add(c)
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
    
    for u in range(1, n + 1):
        seen = set()
        for v, idx in adj[u]:
            seen.add(color[idx])
        if seen != {1, 2, 3}:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()