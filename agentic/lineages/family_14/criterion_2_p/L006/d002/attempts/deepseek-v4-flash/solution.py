import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priority = set(map(int, input().split()))
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # We'll root at 1
    parent = [0]*(n+1)
    parent_cost = [0]*(n+1)
    order = [1]
    parent[1] = -1
    for u in order:
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                parent_cost[v] = w
                order.append(v)
    
    # Count priority nodes in each subtree
    cnt = [0]*(n+1)
    for node in priority:
        cnt[node] = 1
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == 1:
            continue
        p = parent[u]
        cnt[p] += cnt[u]
        if cnt[u] > 0 and cnt[u] < t:
            total_cost += parent_cost[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()