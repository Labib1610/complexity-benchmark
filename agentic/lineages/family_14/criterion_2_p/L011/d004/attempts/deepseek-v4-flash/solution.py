import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    required = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Root at any required node
    root = next(iter(required))
    
    parent = [0] * (n + 1)
    parent_w = [0] * (n + 1)
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
    
    # Count required nodes in subtree
    cnt = [0] * (n + 1)
    for u in required:
        cnt[u] = 1
    
    total_cost = 0
    # Process in reverse order (post-order)
    for u in reversed(order):
        if u == root:
            continue
        p = parent[u]
        cnt[p] += cnt[u]
        # Edge (p, u) is needed if subtree has at least 1 required
        # and not all required are in that subtree
        if cnt[u] > 0 and cnt[u] < t:
            total_cost += parent_w[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()