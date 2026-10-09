import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priority = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # pick a root (any priority node)
    root = next(iter(priority))
    
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_w[v] = w
                stack.append(v)
    
    sub_count = [0] * (n + 1)
    for u in priority:
        sub_count[u] = 1
    
    total = 0
    for u in reversed(order):
        if u == root:
            continue
        p = parent[u]
        sub_count[p] += sub_count[u]
        if sub_count[u] > 0 and sub_count[u] < t:
            total += parent_w[u]
    
    print(total)

if __name__ == "__main__":
    solve()