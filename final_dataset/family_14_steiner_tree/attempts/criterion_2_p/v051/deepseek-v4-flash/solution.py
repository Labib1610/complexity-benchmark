import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    parent = [0] * (n + 1)
    weight = [0] * (n + 1)
    order = [1]
    parent[1] = -1
    for u in order:
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                weight[v] = w
                order.append(v)
    
    cnt = [0] * (n + 1)
    for node in targets:
        cnt[node] = 1
    
    total = 0
    for u in reversed(order):
        if u == 1:
            continue
        if cnt[u] > 0 and (t - cnt[u]) > 0:
            total += weight[u]
        p = parent[u]
        cnt[p] += cnt[u]
    
    print(total)

if __name__ == "__main__":
    solve()