import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    T = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Root at any vertex in T
    root = next(iter(T))
    
    parent = [0]*(n+1)
    parent_w = [0]*(n+1)
    order = []
    stack = [root]
    parent[root] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_w[v] = w
            stack.append(v)
    
    # Count marked in subtree
    cnt = [0]*(n+1)
    for u in T:
        cnt[u] = 1
    
    total = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        p = parent[u]
        cnt[p] += cnt[u]
        if cnt[u] > 0 and cnt[u] < t:
            total += parent_w[u]
    
    print(total)

if __name__ == "__main__":
    solve()