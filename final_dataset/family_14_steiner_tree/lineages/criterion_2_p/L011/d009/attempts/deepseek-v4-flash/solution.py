import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    mandated = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Find a starting mandated node
    start = next(iter(mandated)) - 1
    
    parent = [-1] * n
    parent_w = [0] * n
    order = [start]
    stack = [start]
    parent[start] = start
    
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_w[v] = w
            stack.append(v)
            order.append(v)
    
    cnt = [0] * n
    for x in mandated:
        cnt[x - 1] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u == start:
            continue
        p = parent[u]
        cnt[p] += cnt[u]
        if cnt[u] > 0 and cnt[p] - cnt[u] > 0:
            total_cost += parent_w[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()