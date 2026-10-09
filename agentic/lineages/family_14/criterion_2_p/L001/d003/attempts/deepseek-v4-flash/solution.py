import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    core = set(map(int, input().split()))
    
    g = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
        edges.append((u, v, w))
    
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    order = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    for node in order:
        for nei, w in g[node]:
            if not visited[nei]:
                visited[nei] = True
                parent[nei] = node
                parent_w[nei] = w
                order.append(nei)
    
    core_count = [0] * (n + 1)
    for c in core:
        core_count[c] = 1
    
    total = 0
    for node in reversed(order):
        if node != 1:
            p = parent[node]
            core_count[p] += core_count[node]
            if core_count[node] > 0 and core_count[node] < t:
                total += parent_w[node]
    print(total)

if __name__ == "__main__":
    solve()