import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t == 1:
        print(0)
        return
    
    # DFS to mark nodes that lead to critical
    important = [False] * (n + 1)
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    
    stack = [(next(iter(critical)), -1)]
    order = []
    while stack:
        u, p = stack.pop()
        parent[u] = p
        order.append(u)
        for v, w in adj[u]:
            if v != p:
                parent[v] = u
                parent_w[v] = w
                stack.append((v, u))
    
    # Determine importance
    for u in reversed(order):
        if u in critical:
            important[u] = True
            continue
        for v, w in adj[u]:
            if v != parent[u] and important[v]:
                important[u] = True
                break
    
    total = 0
    for u in range(2, n + 1):
        if important[u]:
            total += parent_w[u]
    
    print(total)

if __name__ == "__main__":
    solve()