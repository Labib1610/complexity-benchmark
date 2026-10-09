import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    keys = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    parent = [-1] * n
    parent_w = [0] * n
    order = [0]
    parent[0] = -2  # root marker
    
    # Build parent and order via stack
    stack = [0]
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_w[v] = w
            stack.append(v)
            order.append(v)
    
    sub_count = [0] * n
    for u in range(n):
        if u + 1 in keys:
            sub_count[u] = 1
    
    # Process in reverse order (post-order)
    total = 0
    for u in reversed(order):
        if u == 0:
            continue
        p = parent[u]
        sub_count[p] += sub_count[u]
        if 0 < sub_count[u] < t:
            total += parent_w[u]
    
    print(total)

if __name__ == "__main__":
    solve()