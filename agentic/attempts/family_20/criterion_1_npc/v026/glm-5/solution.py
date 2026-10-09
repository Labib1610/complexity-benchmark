import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    edges = []
    for i in range(m):
        u = int(input_data[2 + 2*i])
        v = int(input_data[3 + 2*i])
        edges.append((u, v))
    
    adj = [[] for _ in range(n + 1)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    color = [0] * m
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
        stack = [(start, 0, 0)]
        visited[start] = True
        while stack:
            node, parent, c = stack.pop()
            for (nbr, eidx) in adj[node]:
                if eidx == parent:
                    continue
                if not visited[nbr]:
                    visited[nbr] = True
                    color[eidx] = c
                    stack.append((nbr, eidx, (c + 1) % 3))
                else:
                    if color[eidx] == 0:
                        color[eidx] = c
    
    for u in range(1, n + 1):
        seen = set()
        for (nbr, eidx) in adj[u]:
            seen.add(color[eidx])
        if seen != {0, 1, 2}:
            print("NO")
            return
    
    print("YES")
    print(' '.join(str(c + 1) for c in color))

solve()