import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    flagged = [False] * (n + 1)
    for _ in range(t):
        flagged[int(next(it))] = True
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    parent = [0] * (n + 1)
    parent_edge_weight = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = 0
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_edge_weight[v] = w
                stack.append(v)
    
    dp = [0] * (n + 1)
    has_flagged = [False] * (n + 1)
    
    for u in order[::-1]:
        has_flagged[u] = flagged[u]
        for v, w in adj[u]:
            if v != parent[u]:
                if has_flagged[v]:
                    dp[u] += dp[v] + w
                    has_flagged[u] = True
    
    total = 0
    for u in order:
        if u == 1:
            continue
        if has_flagged[u]:
            cnt = 0
            for v, w in adj[u]:
                if v != parent[u] and has_flagged[v]:
                    cnt += 1
            if cnt > 0 or flagged[u]:
                total += parent_edge_weight[u]
    
    print(total)

if __name__ == "__main__":
    solve()