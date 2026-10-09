import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to find which edges are needed
    # We'll root at any critical node, say first one
    root = next(iter(critical))
    
    parent = [-1] * n
    parent_edge_cost = [0] * n
    stack = [(root, -1)]
    order = []
    while stack:
        u, p = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v == p:
                continue
            parent[v] = u
            parent_edge_cost[v] = w
            stack.append((v, u))
    
    # Post-order: determine if subtree contains critical node
    has_critical = [False] * n
    for u in critical:
        has_critical[u] = True
    
    total_cost = 0
    for u in reversed(order):
        if u == root:
            continue
        if has_critical[u]:
            total_cost += parent_edge_cost[u]
            # propagate up
            p = parent[u]
            has_critical[p] = True
    
    print(total_cost)

if __name__ == "__main__":
    solve()