import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    primaries = list(map(int, input().split()))
    primary_set = set(primaries)
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    if t <= 1:
        print(0)
        return
    
    parent = [-1] * n
    parent_weight = [0] * n
    order = [0]
    stack = [0]
    parent[0] = -2  # root marker
    
    # Build parent and order via iterative DFS
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_weight[v] = w
            stack.append(v)
    
    # Count primary nodes in each subtree
    sub_count = [0] * n
    for p in primaries:
        sub_count[p] = 1
    
    # Process in reverse order (post-order)
    total_cost = 0
    for u in reversed(order):
        if u == 0:
            continue
        p = parent[u]
        # If subtree has at least one primary and outside has at least one primary
        if sub_count[u] > 0 and (t - sub_count[u]) > 0:
            total_cost += parent_weight[u]
        sub_count[p] += sub_count[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()