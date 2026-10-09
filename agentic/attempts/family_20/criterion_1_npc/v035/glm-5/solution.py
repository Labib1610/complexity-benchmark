import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    color = [0] * m
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        for v, e_idx in adj[u]:
            if color[e_idx] == 0:
                used = {0}
                for x, e2 in adj[u]:
                    if color[e2] != 0:
                        used.add(color[e2])
                for x, e2 in adj[v]:
                    if color[e2] != 0:
                        used.add(color[e2])
                for c in range(1, 4):
                    if c not in used:
                        color[e_idx] = c
                        break
                if color[e_idx] == 0:
                    return False
                if not visited[v]:
                    if not dfs(v):
                        return False
        return True
    
    for i in range(1, n + 1):
        if not visited[i]:
            if not dfs(i):
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, color)))

solve()